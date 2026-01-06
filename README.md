# 💎 Global Finance Automation & Capital Efficiency Platform

## 🎯 Executive Overview
This platform is an enterprise-grade financial engineering solution designed to consolidate multi-currency subsidiary data into a single, auditable USD "Source of Truth." 

The system replaces fragmented, manual spreadsheets with a deterministic Python pipeline that enables **ROIC (Return on Invested Capital)** benchmarking and executive-level capital allocation decisions across 6 global jurisdictions (ZAR, CHF, GBP, BRL, INR, EUR).

---

## ⚙️ Solution Architecture
The platform implements a modular ETL (Extract, Transform, Load) architecture:

1.  **`pipeline.py` (The ETL Engine):** - Ingests raw subsidiary ledgers.
    - Handles "Malformed Hybrid" data (Excel files containing comma-separated strings).
    - Executes deterministic FX normalization.
    - Standardizes disparate Charts of Accounts (CoA) via `dim_Mapping_Logic`.

2.  **`analytics.py` (Executive Intelligence):** - Consumes the consolidated master fact table.
    - Derives NOPAT (Net Operating Profit After Tax) and Invested Capital.
    - Benchmarks entities against a 10% target hurdle rate.

---

## 🛠 Technical Challenge: The "Data Integrity" Recovery
**The Problem:** Initial data ingestion resulted in a "False Zero" ROIC for 5 out of 6 entities. This was caused by malformed hybrid source files—Excel extensions containing single-column comma-separated values—which prevented the Join-Key from mapping to the master logic.

**The Fix:** - Implemented a **Preprocessing String-Splitting Layer** to "unpack" the hybrid files.
- Developed a **Brute-Force Column Normalizer** to handle inconsistent header naming (e.g., `Account Code` vs `ACCOUNTCODE`).
- **Result:** Recovered full data visibility, identifying **CryptoFlow (Brazil)** as a high-efficiency star with a **167.86% ROIC**.

---

## 🧮 Financial Engineering Logic
- **NOPAT:** EBIT adjusted for a 25% weighted-average jurisdictional tax assumption.
- **Invested Capital:** Balance-sheet driven capital employed calculation.
- **ROIC:** Primary capital efficiency metric used to distinguish value-creators from capital-dilutive entities.

---

## 🚀 How to Run
1. **Prepare Data:** Ensure raw ledgers are in the `/data` folder.
2. **Execute Pipeline:** ```bash
   python pipeline.py
   