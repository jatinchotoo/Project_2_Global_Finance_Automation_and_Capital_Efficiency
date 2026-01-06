import pandas as pd
import numpy as np
import os

# Point to the data folder
base_path = os.path.join(os.getcwd(), 'data')
master_file = os.path.join(base_path, "Master_Consolidated_Fact.csv")

print("--- GENERATING EXECUTIVE ROIC REPORT ---")

try:
    df = pd.read_csv(master_file)
    
    # Grouping
    pivot = df.pivot_table(index='Entity', columns='Group_Category', values='Amount_USD', aggfunc='sum').fillna(0)
    
    # Financial Formulas
    pivot['EBIT'] = pivot['Revenue'] - pivot['OpEx']
    pivot['NOPAT'] = pivot['EBIT'] * 0.75 
    pivot['ROIC_%'] = (pivot['NOPAT'] / pivot['Assets'].replace(0, np.nan)) * 100

    print("\n" + "="*65)
    print("             GLOBAL ALPHA PORTFOLIO STRATEGY REPORT")
    print("="*65)
    report = pivot[['Revenue', 'NOPAT', 'Assets', 'ROIC_%']].sort_values(by='ROIC_%', ascending=False)
    print(report.round(2))
    print("="*65)
    
    # --- EXPORT SECTION ---
    # Save to CSV and Excel
    report.to_csv(os.path.join(base_path, 'Final_ROIC_Report.csv'))
    report.to_excel(os.path.join(base_path, 'Executive_Performance_Summary.xlsx'))
    
    print("✅ Reports exported to /data/ folder.")
    print("✅ ANALYSIS COMPLETE")

except FileNotFoundError:
    print("❌ Error: Master_Consolidated_Fact.csv not found. Run pipeline.py first!")