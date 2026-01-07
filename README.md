# 💎 Global Finance & ROIC: Capital Efficiency Engine

<p align="center">
  <img src="images/roic.png" width="80%" alt="ROIC Benchmarking">
</p>

## 🎯 Executive Overview
This platform is an enterprise-grade financial engineering solution designed to consolidate multi-currency subsidiary data into a single, auditable USD "Source of Truth." It automates the extraction of raw ledgers to calculate **ROIC (Return on Invested Capital)**, enabling executive-level benchmarking across global jurisdictions.

---

## 📂 Repository Structure
```text
Project_2_Global_Finance_Automation/
├─ images/
│  ├─ roic.png
│  └─ roic_results.png
├─ data/
│  ├─ Master_Consolidated_Fact.csv
│  └─ Executive_Performance_Summary.xlsx
├─ pipeline.py
├─ analytics.py
└─ README.md
⚙️ Solution Architecture
The system follows a modular ETL (Extract, Transform, Load) design:

pipeline.py (The ETL Engine): Executes Fuzzy Matching and Column Normalization to align disparate regional charts of accounts. Applies deterministic FX translation logic.

analytics.py (Executive Intelligence): Calculates NOPAT and Invested Capital. Generates automated performance visuals and audit trails.

📊 Performance Intelligence
Executive Summary (Raw Terminal Output)
<p align="center"> <img src="images/roic_results.png" width="80%" alt="Terminal Results"> </p>

Top Performer: CryptoFlow achieves an elite 167.86% ROIC, demonstrating extreme capital efficiency.

Strategic Risk: Terra-Grid flags $2.1M in idle assets (Assets: 2,100,000.0) with 0.00% ROIC, triggering an immediate capital reallocation review.

Data Governance: The system identifies entities with missing Balance Sheet data (marked as NaN), such as FinShield Re and Omni-Retail, to streamline internal audits.

🛠 Technical Challenge: The "Data Integrity" Recovery
The Problem: Initial data ingestion resulted in a "False Zero" ROIC due to malformed hybrid files and inconsistent column naming (e.g., Revenue vs REVENUE).

The Fix: Implemented a Preprocessing String-Splitting Layer to "unpack" the hybrid CSV data and developed a Case-Insensitive Column Normalizer.

🚀 How to Run
Prepare Data: Ensure raw ledgers are located in the /data folder.

Execute Pipeline: python pipeline.py

Generate Analytics: python analytics.py

Author: Jatin Chotoo

Focus: Python Automation, Capital Efficiency, and Strategic Finance