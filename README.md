# 💎 Global Finance Automation & Capital Efficiency Platform

## 🎯 Executive Overview
This platform is an enterprise-grade financial engineering solution designed to consolidate multi-currency subsidiary data into a single, auditable USD "Source of Truth." It automates the extraction of raw ledgers to calculate **ROIC (Return on Invested Capital)**, enabling executive-level benchmarking across 6 global jurisdictions.

---

## 📂 Repository Structure
```text
Project_2_Global_Alpha_Clean/
├─ data/
│  ├─ Master_Consolidated_Fact.csv
│  ├─ Final_ROIC_Report.csv
│  └─ Executive_Performance_Summary.xlsx
├─ images/
│  ├─ roic.png
│  └─ roic_results.png
├─ pipeline.py
├─ analytics.py
└─ README.md

## ⚙️ Solution Architecture
The system follows a modular ETL (Extract, Transform, Load) design:

1.  **`pipeline.py` (The ETL Engine):** * Ingests raw subsidiary ledgers (Excel/CSV).
    * Executes **Fuzzy Matching** and **Column Normalization** to align disparate regional charts of accounts.
    * Applies deterministic FX translation logic.
2.  **`analytics.py` (Executive Intelligence):** * Pivots "Long-Format" ledger data to isolate Revenue and Assets.
    * Calculates **NOPAT** and **Invested Capital**.
    * Generates automated Excel/CSV audit trails and performance visuals.

---

## 📊 Performance Intelligence

### **Executive Summary (Raw Terminal Output)**
![Terminal ROIC Results](images/roic_results.png)

### **Visual Benchmarking**
![ROIC Analysis](images/roic.png)

* **Top Performer:** **CryptoFlow (Brazil)** achieves an elite **167.86% ROIC**, demonstrating extreme capital efficiency.
* **Strategic Risk:** **Terra-Grid** flags **$2.1M in idle assets** with 0% current yield, triggering an immediate capital reallocation review.
* **Data Governance:** The system automatically identifies entities with missing Balance Sheet data (marked as **NaN**), streamlining the internal audit process.

---

## 🛠 Technical Challenge: The "Data Integrity" Recovery
**The Problem:** Initial data ingestion resulted in a "False Zero" ROIC due to malformed hybrid files (files with `.xlsx` extensions that actually contained raw CSV strings) and inconsistent column naming (e.g., `Revenue` vs `REVENUE`).

**The Fix:** * Implemented a **Preprocessing String-Splitting Layer** to "unpack" the hybrid CSV data.
* Developed a **Case-Insensitive Column Normalizer** and a **Pivot Filter** to correctly identify financial metrics regardless of how the local accounting software exported the headers.

---

## ⚖️ Governance & FX Methodology

### **FX Normalization Logic**
* **Balance Sheet (Invested Capital):** Applied **Spot Rate** at period-end for accurate valuation of capital at risk.
* **P&L (NOPAT):** Applied **Average Rate** over the reporting period to reflect operational flow.
* **Audit Trail:** All USD conversions are logged with timestamped exchange rates to ensure full auditability.

### **Automated Controls**
* **Schema Validation:** Ensures data types (Float/Int) match before aggregation to prevent calculation crashes.
* **Null-Value Gating:** Prevents divide-by-zero errors in the ROIC engine.
* **Reconciliation:** Automated check of "Total Local Amount" vs "Total USD" to ensure zero data loss during the transformation.

---

## 🚀 How to Run
1.  **Prepare Data:** Ensure raw ledgers are located in the `/data` folder.
2.  **Execute Pipeline:** ```powershell
    python pipeline.py
    ```
3.  **Generate Analytics:** ```powershell
    python analytics.py
    ```
4.  **Review Outputs:** Check the `/images` folder for charts and `/data/Executive_Performance_Summary.xlsx` for the final report.

---
**Author:** Jatin Chotoo  
**Role:** Financial Data Engineer / Analyst  
**Focus:** Python Automation, Capital Efficiency, and Strategic Finance