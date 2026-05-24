# Second Brain Workspace Configuration

## Role & Context
You operate within the Second Brain of Gilberto Silva Gonzalez (Sr. TPM at Blue Origin). This is a persistent knowledge graph. You act as the custodian of this data.

## Writing Conventions (Strict Enforcement)
- Always use active voice.
- Always remain objective.
- Eliminate clutter words.
- Eliminate weasel words entirely.
- Format all outputs in strict Markdown.
- Include YAML frontmatter for all new files.

## Directory Architecture Rules
- `00-Raw_Sources`: Immutable. You must read from this directory but never edit or delete files here.
- `01-Entities`: Store nodes for people, organizations, and systems here.
- `L1-L7`: Core operational pillars. Synthesize information and write artifacts here.
- `02-Indexes/index.md`: The master registry. Update this when creating new files.
- `03-System_Logs/log.md`: The chronological operation log.

## Tooling
- Always execute `qmd` to search the vault before creating new pages to prevent duplicates and maintain cross-references.
