// Function Health bulk extractor. Paste the whole file into mcp__claude-in-chrome__javascript_tool
// while a logged-in my.functionhealth.com tab is in the FOREGROUND (background tabs are throttled).
//
// It starts a background job and returns immediately. Poll with:
//   ({prog: window.__fhProg, n: Object.keys(window.__fhBundle).length, err: window.__fhErrors})
// Stop with `window.__fhKill = true`. Re-pasting the script resumes: finished entries stay in
// window.__fhBundle and are skipped.
// When prog.running is false, call `window.__fhDownload()` to save function-health-biomarkers.json.
(() => {
  const SITE = 'https://my.functionhealth.com';
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const y = (s) => JSON.stringify(String(s));
  const last = (h) => h.split('/').pop();
  const fileSlug = (h) => last(h).replace(/%25/g, 'percent').replace(/-+/g, '-');
  const catSlug = (s) => s.toLowerCase().replace(/[()]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const go = async (href) => {
    history.pushState({}, '', href);
    window.dispatchEvent(new PopStateEvent('popstate', { state: {} }));
  };

  // --- Redux store, found through the React fiber tree under #app ---
  const findStore = () => {
    const root = document.getElementById('app');
    const key = Object.keys(root).find((k) => k.startsWith('__reactContainer'));
    const seen = new Set();
    const stack = [root[key]];
    while (stack.length) {
      const f = stack.pop();
      if (!f || seen.has(f)) continue;
      seen.add(f);
      const p = f.memoizedProps;
      if (p && p.store && typeof p.store.getState === 'function') return p.store;
      if (f.child) stack.push(f.child);
      if (f.sibling) stack.push(f.sibling);
    }
    return null;
  };

  // --- DOM -> Markdown (page sections only) ---
  const inline = (n) => {
    if (n.nodeType === 3) return n.textContent;
    if (n.nodeType !== 1) return '';
    const t = n.tagName;
    const c = [...n.childNodes].map(inline).join('');
    if (t === 'STRONG' || t === 'B') return c.trim() ? `**${c.trim()}** ` : '';
    if (t === 'EM' || t === 'I') return c.trim() ? `*${c.trim()}*` : '';
    if (t === 'A' && n.href && !n.href.startsWith('javascript')) return `[${c.trim()}](${n.href})`;
    if (t === 'BR') return '\n';
    return c;
  };
  const block = (n, depth = 0) => {
    if (n.nodeType === 3) return n.textContent.trim() ? n.textContent.trim() + '\n\n' : '';
    if (n.nodeType !== 1) return '';
    const t = n.tagName;
    if (t === 'H4') return '';
    if (/^H[1-6]$/.test(t)) return `### ${n.innerText.trim()}\n\n`;
    if (t === 'P') {
      const s = inline(n).replace(/\*\* +/g, '** ').trim();
      return s ? s + '\n\n' : '';
    }
    if (t === 'UL' || t === 'OL') {
      return [...n.children].filter((li) => li.tagName === 'LI').map((li, i) => {
        const sub = [...li.children].filter((c) => c.tagName === 'UL' || c.tagName === 'OL');
        const own = [...li.childNodes].filter((c) => !sub.includes(c)).map(inline).join('').replace(/\s+/g, ' ').trim();
        return '  '.repeat(depth) + (t === 'OL' ? `${i + 1}. ` : '- ') + own + '\n' + sub.map((s) => block(s, depth + 1)).join('');
      }).join('') + (depth ? '' : '\n');
    }
    if (['IMG', 'SVG', 'svg', 'BUTTON'].includes(t)) return '';
    return [...n.childNodes].map((c) => block(c, depth)).join('');
  };
  // The page renders every section twice (sidebar nav + content). Drop the banner h4 on
  // out-of-range pages ("Re-test Out of Range Biomarker"), then take the second half.
  const grab = () => {
    const hs = [...document.querySelectorAll('h4')].filter((x) => !/^Re-test/i.test(x.innerText.trim()));
    if (!hs.length || hs.length % 2) return null;
    const half = hs.length / 2;
    const a = hs.slice(0, half).map((x) => x.innerText.trim()).join('|');
    const b = hs.slice(half).map((x) => x.innerText.trim()).join('|');
    if (a !== b) return null;
    return hs.slice(half).map((x) => ({
      name: x.innerText.trim(),
      md: `## ${x.innerText.trim()}\n\n` + block(x.parentElement).replace(/\n{3,}/g, '\n\n').trim() + '\n',
    }));
  };

  // --- one Markdown file per biomarker ---
  const build = (r, cat, path, secs, details) => {
    const b = r.biomarker;
    const rs = (r.biomarkerResults || []).filter((x) => x.visible !== false)
      .sort((p, q) => p.dateOfService.localeCompare(q.dateOfService));
    const cur = r.currentResult;
    const prev = r.previousResult;
    const det = details.find((d) => d.biomarkerId === b.id);
    const crit = det && det.critical;
    const unit = r.units || (rs[0] && rs[0].measurementUnits) || '';
    const cls = (r.interpretation && r.interpretation.classification) || r.outOfRangeType || '';
    const fm = ['---', `title: ${y('Function Health — ' + b.name)}`, 'type: raw-source', 'platform: Function Health',
      `source_url: ${SITE}${path}`, `captured: ${new Date().toISOString().slice(0, 10)}`,
      `extraction_method: Claude in Chrome (results from app store, sections from rendered page)`,
      `biomarker: ${y(b.name)}`, `category: ${y(cat)}`, `unit: ${y(unit)}`, 'lab: Quest',
      cur ? `current_result: {date: ${cur.dateOfService}, value: ${y(cur.displayResult)}, status: ${y(cls || (cur.inRange ? 'in-range' : 'out-of-range'))}}` : 'current_result: null',
      prev ? `previous_result: {date: ${prev.dateOfService}, value: ${y(prev.displayResult)}, status: ${y(prev.inRange ? 'in-range' : 'out-of-range')}}` : 'previous_result: null',
      `result_count: ${rs.length}`, `quest_reference_range: ${y(r.rangeString || '')}`,
      `function_optimal_range: ${y(r.optimalRange || (r.optimalRangeMin || '') + '-' + (r.optimalRangeMax || ''))}`,
      `critical_priority_1: ${y(crit && crit.priority1Range ? crit.priority1Range.join(', ') : '')}`,
      `critical_priority_2: ${y(crit && crit.priority2Range ? crit.priority2Range.join(', ') : '')}`,
      `sections: [${secs.map((s) => y(s.name)).join(', ')}]`, '---', ''].join('\n');
    const hi = r.rangeMaxDisplay;
    const lo = r.rangeMinDisplay;
    const bands = [hi ? `| Above range | > ${hi} ${unit} |` : null, `| In range | ${r.rangeString || 'n/a'} ${unit} |`,
      lo ? `| Below range | < ${lo} ${unit} |` : null].filter(Boolean).join('\n');
    const rows = rs.map((x) => `| ${x.dateOfService} | ${x.testResult} ${x.measurementUnits || ''} | ${x.testResultOutOfRange ? 'Out of range' : 'In range'} | ${x.questReferenceRange || ''} |`).join('\n');
    const body = `# ${b.name}\n\n${(b.oneLineDescription || '').replace(/\s+/g, ' ').trim()}\n\n## My results\n\n` +
      `| Date | Result | Status | Quest reference range |\n|---|---|---|---|\n${rows}\n\n## Range bands\n\n| Band | Range |\n|---|---|\n${bands}\n\n` +
      `Function Health optimal range: ${r.optimalRange || 'n/a'}.\n\n`;
    return fm + body + (secs.length ? secs.map((s) => s.md).join('\n') : 'This biomarker page has no description sections on Function Health.\n');
  };

  window.__fhDownload = () => {
    const blob = new Blob([JSON.stringify(window.__fhBundle)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'function-health-biomarkers.json';
    document.body.appendChild(a);
    a.click();
    a.remove();
    return 'download started';
  };

  window.__fhBundle = window.__fhBundle || {};
  window.__fhErrors = {};
  window.__fhKill = false;
  window.__fhProg = { phase: 'start', done: Object.keys(window.__fhBundle).length, total: 0, running: true, current: '', visibility: document.visibilityState };

  (async () => {
    try {
      const store = findStore();
      if (!store) throw new Error('Redux store not found: open any my.functionhealth.com page first');
      const q = () => store.getState().api.queries;
      const rk = Object.keys(q()).find((k) => k.startsWith('getResultsReport'));
      if (!rk) throw new Error('getResultsReport not in store: reload the page and retry');
      const recs = q()[rk].data.biomarkerResultsRecord;
      const details = q()['getBiomarkerDetails(undefined)'].data;
      window.__fhProg.total = recs.length;
      window.__fhLatestDraw = recs.map((r) => r.currentResult && r.currentResult.dateOfService).filter(Boolean).sort().pop();

      // 1. Real page URLs come from the category pages. Slugs are not derivable (`%` stays `%25`,
      //    "Arachidonic Acid/EPA Ratio" -> arachidonic-acidepa-ratio), so read the links.
      window.__fhProg.phase = 'crawling category pages';
      const cats = [...new Set(recs.map((r) => r.biomarker.categories && r.biomarker.categories[0] && r.biomarker.categories[0].categoryName).filter(Boolean))];
      const links = [];
      for (const c of cats) {
        if (window.__fhKill) return;
        await go('/biomarkers/' + catSlug(c));
        await sleep(2500);
        document.querySelectorAll(`a[href^="/biomarkers/${catSlug(c)}/"]`).forEach((a) =>
          links.push({ href: a.getAttribute('href'), text: a.innerText.trim().replace(/\s+/g, ' ') }));
      }
      const names = recs.map((r) => r.biomarker.name).sort((a, b) => b.length - a.length); // longest first
      const hrefOf = {};
      for (const l of links) {
        const n = names.find((nm) => l.text === nm || l.text.startsWith(nm + ' '));
        if (n && !hrefOf[n]) hrefOf[n] = l.href;
      }
      window.__fhHrefOf = hrefOf;

      // 2. Visit each page, wait for the sections to render, build the file.
      window.__fhProg.phase = 'extracting';
      let prevH1 = '';
      for (const r of recs) {
        if (window.__fhKill) break;
        const b = r.biomarker;
        const href = hrefOf[b.name];
        if (!href) { window.__fhErrors[catSlug(b.name)] = 'no page href (record has no biomarker page)'; continue; }
        const key = fileSlug(href);
        if (window.__fhBundle[key]) continue;
        window.__fhProg.current = b.name;
        window.__fhProg.visibility = document.visibilityState;
        const cat = (b.categories && b.categories[0] && b.categories[0].categoryName) || '';
        try {
          if (decodeURI(location.pathname) !== decodeURI(href)) await go(href);
          let secs = null;
          let stable = 0;
          let lastSig = '';
          const t0 = Date.now();
          while (Date.now() - t0 < 40000) {
            await sleep(500);
            const h1 = [...document.querySelectorAll('h1')].map((x) => x.innerText.trim()).find(Boolean) || '';
            if (!h1 || h1 === prevH1) continue; // stale page from the previous biomarker
            const g = grab();
            if (g) {
              const sig = h1 + '|' + g.map((x) => x.md.length).join(',');
              stable = sig === lastSig ? stable + 1 : 0;
              lastSig = sig;
              if (stable >= 2) { secs = g; prevH1 = h1; break; }
            } else if (!document.querySelectorAll('h4').length && Date.now() - t0 > 12000) {
              secs = []; prevH1 = h1; break; // results-only page, e.g. "White Blood Cell (WBC) - Urine"
            }
          }
          if (!secs) throw new Error('sections did not render');
          window.__fhBundle[key] = build(r, cat, href, secs, details);
        } catch (e) {
          window.__fhErrors[key] = String(e.message || e);
        }
        window.__fhProg.done = Object.keys(window.__fhBundle).length;
        await sleep(800);
      }
    } catch (e) {
      window.__fhErrors._fatal = String(e.message || e);
    }
    window.__fhProg.phase = 'finished';
    window.__fhProg.running = false;
  })();
  return 'started';
})();
