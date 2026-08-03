# **Financial Schema and Category Definition for Expenses**

The following document defines the financial categorization schema for Gil and Lu. It is designed to be ingested by AI agents to understand the exact structure, rules, and logic applied to their household finances. All future transaction sorting, budgeting, and financial analysis must adhere to the rules and definitions outlined in this schema.

## **Section 1: Main Category Groups (Routing Rules)**

Financial transactions are routed into one of five primary groups. The AI must use the following rules to classify incoming data.

1. **NEEDS:** This group encompasses all essential expenses required for basic living and maintaining the current household. These are non-negotiable costs.  
   * **Routing Rule:** Classify a transaction here if it is required for survival, shelter, basic utilities, mandatory insurance, or essential health. Do not include lifestyle upgrades or discretionary spending in this group.  
2. **WANTS JOINT:** This category covers discretionary spending shared between Gil and Lu. These are expenses that enhance lifestyle but are not strictly necessary for survival.  
   * **Routing Rule:** Classify a transaction here if it represents shared entertainment, dining, travel, or convenience services used by both individuals. This includes shared subscriptions and joint social outings.  
3. **SAVINGS / DEBT:** This group reflects financial obligations related to past borrowing and future security.  
   * **Routing Rule:** Classify a transaction here if it represents a payment toward outstanding debt principal/interest, minimum credit card payments, or outgoing transfers to retirement, investment, or savings accounts.  
4. **PERSONAL LU:** This category tracks the individual, discretionary spending specific to Lu.  
   * **Routing Rule:** Classify a transaction here if the expense is solely for Lu's personal enjoyment, personal care, individual family support, or individual business expenses, separate from joint household funds.  
5. **PERSONAL GIL:** This category tracks the individual, discretionary spending specific to Gil.  
   * **Routing Rule:** Classify a transaction here if the expense is solely for Gil's personal enjoyment, personal care, individual family support, or individual shopping, separate from joint household funds.

## **Section 2: Schema Data Dictionary: Subcategory Definitions**

This section provides the strict data dictionary for subcategories. The AI must map transactions to these specific subcategories based on the descriptions below.

### **Group: NEEDS**

* **Car \+ Gas:** Expenses related to vehicle ownership, including fuel and maintenance.  
  * *\[SYSTEM NOTE\]:* Gil and Lu returned their Nissan Kicks lease in March; currently, they only own the Mazda.  
  * *\[DATA TAGGING RULE\]:* Individual gas transactions must be explicitly labeled as "gas" to track fuel spending separately from other car maintenance.  
* **Home Everbe:** Expenses related to the current "Everbe" property/housing situation (closed on June 2).  
  * *\[ROUTING RULE\]:* This category is STRICTLY for HOA fees, maintenance, and furniture. It does NOT include the mortgage payment.  
* **Groceries:** Essential food and household items purchased from supermarkets or grocery stores.  
* **Phones:** Monthly cellular service plans and device payment installments.  
* **Luna:** Expenses related to the pet "Luna" (food, veterinary care, grooming, supplies).  
* **Insurance:** Premiums for auto, health, renters/homeowners, or life insurance policies.  
* **Electricity:** Monthly utility bill for electrical service.  
* **Healthcare:** Out-of-pocket medical expenses, copays, prescriptions, and services not fully covered by insurance.  
  * *\[SYSTEM NOTE\]:* This category includes recurring medical/dermatological subscription plans (e.g., Lu's recurring face treatments and acne treatments).  
* **CIRRUS (Rent \+ Water ...):** Rent and integrated utility payments (like water) for the previous "CIRRUS" apartment property.  
  * *\[SYSTEM NOTE\]:* Gil and Lu stopped living at Cirrus on June 8\. This category exists for historical data routing prior to that date to separate it from "Home Everbe" expenses.  
* **Mortgage:** Monthly payments towards the home loan for the Everbe property, including principal and interest.  
  * *\[SYSTEM NOTE\]:* The first payment of $3,200 is scheduled for August 1 (explaining zero balances for this subcategory in June/July data).

### **Group: WANTS JOINT**

* **Travel & Vacation:** Comprehensive costs associated with trips, including flights, accommodations, and in-destination activities (e.g., museums, restaurants, nightlife).  
  * *\[DATA TAGGING RULE\]:* The AI must look for and apply explicit labels ("Gil" or "Lu") for travel/vacation expenses incurred individually. If unlabeled, assume it is joint shared travel.  
* **Restaurants \- Joint:** Dining out together, which explicitly includes ordering food delivery to the house.  
* **Bars & Nightlife \- Joint:** Entertainment, drinks, and social outings at bars or clubs attended together.  
* **Subscriptions:** Recurring fees for shared services (streaming platforms, software, magazines).  
* **Other:** Miscellaneous joint discretionary spending that falls outside defined subcategories.  
* **Transportation (Uber):** Ride-sharing services used jointly for convenience.  
* **Entertainment:** Shared activities such as movies, concerts, or recreational events.  
  * *\[SYSTEM NOTE\]:* This category is largely inactive. The AI should attempt to route standard lifestyle expenses into alternative appropriate subcategories (like Bars & Nightlife or Travel) unless explicitly instructed otherwise.  
* **Sports:** Expenses related to joint sporting activities, equipment, or events.  
* **Eight Sleep \- Affirm:** Financed payments for the "Eight Sleep" intelligent mattress product via Affirm.  
  * *\[SYSTEM NOTE\]:* This loan was fully paid off in May. The AI should not expect active or recurring monthly charges here.  
* **Immigration:** Legal fees, applications, or processes concerning immigration status.  
  * *\[SYSTEM NOTE\]:* Not actively being used at this time. Historically utilized for Lu's Green Card; reserved for future use (e.g., Gil's citizenship applications).

### **Group: SAVINGS / DEBT**

* **Loans:** Payments made towards outstanding personal, or other types of loans.  
* **CC min payments:** Minimum required monthly payments on credit card balances.  
* **Retirement:** Contributions to retirement accounts like MPI account.

### **Group: PERSONAL LU**

* **Bar & Restaurants Lu:** Lu's individual spending on dining out or drinks.  
* **Family Lu:** Financial support or gifts sent by Lu to their family.  
* **Shops & Clothing Lu:** Lu's personal discretionary spending on apparel and accessories.  
* **Lu Recruitment Business:** Expenses related to Lu's recruitment business/professional endeavors.  
* **Personal Care Lu:** Spending by Lu on grooming, haircuts, cosmetics, or wellness.

### **Group: PERSONAL GIL**

* **Family Gil:** Financial support or gifts sent by Gil to their family (often associated with Mexico).  
* **Shops & Clothing Gil:** Gil's personal discretionary spending on apparel and accessories.  
* **Personal Image Gil:** Spending by Gil on grooming, haircuts, or personal maintenance.  
* **Bar & Restaurants Gil:** Gil's individual spending on dining out or drinks.

## **Section 3: Data Ingestion Sample (Snapshot)**

The following table is a snapshot of historical data (July). AI should use this to understand the expected data structure, currency formatting (USD), and relationships between Main Categories and Subcategories. Do not treat these values as fixed budgets.

| Main Category | Subcategory | Amount Spent | Total for Main Category |
| :---- | :---- | :---- | :---- |
| **NEEDS** |  |  | **$3,862.35** |
|  | Car \+ Gas | $1,396.16 |  |
|  | Home Everbe | $1,165.43 |  |
|  | Groceries | $583.68 |  |
|  | Phones | $341.54 |  |
|  | Luna | $102.35 |  |
|  | Insurance | $101.24 |  |
|  | Electricity | $87.28 |  |
|  | Healthcare | $84.67 |  |
|  | CIRRUS (Rent \+ Water ...) | $0.00 |  |
|  | Mortgage | $0.00 |  |
| **WANTS JOINT** |  |  | **$5,983.39** |
|  | Travel & Vacation | $1,854.56 |  |
|  | Restaurants \- Joint | $1,737.19 |  |
|  | Bars & Nightlife \- Joint | $1,470.33 |  |
|  | Subscriptions | $644.73 |  |
|  | Other | $225.49 |  |
|  | Transportation (Uber) | $51.09 |  |
|  | Entertainment | $0.00 |  |
|  | Sports | $0.00 |  |
|  | Eight Sleep \- Affirm | $0.00 |  |
|  | Immigration | $0.00 |  |
| **SAVINGS / DEBT** |  |  | **$5,992.81** |
|  | Loans | $4,465.62 |  |
|  | CC min payments | $802.19 |  |
|  | Retirement | $725.00 |  |
| **PERSONAL LU** |  |  | **$130.55** |
|  | Bar & Restaurants Lu | $130.55 |  |
|  | Family Lu | $0.00 |  |
|  | Shops & Clothing Lu | $0.00 |  |
|  | Lu Recruitment Busine... | $0.00 |  |
|  | Personal Care Lu | $0.00 |  |
| **PERSONAL GIL** |  |  | **$383.18** |
|  | Family Gil | $383.18 |  |
|  | Shops & Clothing Gil | $0.00 |  |
|  | Personal Image Gil | $0.00 |  |
|  | Bar & Restaurants Gil | $0.00 |  |
| **TOTAL MONTHLY SPEND (SAMPLE)** |  |  | **$16,352.28** |

