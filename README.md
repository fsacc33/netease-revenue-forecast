# NetEase Quarterly Revenue Forecast Tool

## 1. Problem & User
This tool helps investors and financial analysts quickly estimate NetEase's future quarterly revenue based on historical trends, without complex financial modeling.

## 2. Data
- Source: WRDS Compustat database (fundq table)
- Access date: April 2026
- Key fields: datadate (quarter end date), revtq (quarterly revenue in million USD), tic (ticker NTES)
- Time range: 2016 Q1 - 2025 Q4 (40 quarters)

## 3. Methods
1. Load quarterly revenue data from CSV file
2. Clean data: remove missing values, sort by date
3. Convert dates to sequential quarter numbers (1,2,3...)
4. Train linear regression model: Revenue ~ Quarter Number
5. Predict future revenue
6. Display results as table and trend chart

## 4. Key Findings
- NetEase's quarterly revenue shows a clear upward trend from 2016 to 2025
- Linear model R² score: 0.87 (model explains 87% of revenue variation)
- Average quarterly revenue growth: approximately $68 million per quarter
- Forecast for next 4 quarters: $4,325M - $4,533M
- Revenue has grown from ~$1,200M in 2016 to ~$4,100M in 2025

## 5. How to Run Locally
```bash
pip install streamlit pandas numpy scikit-learn matplotlib
streamlit run "netease revenue predict.py"

## 6. Product Link
https://netease-revenue-forecast-95q4hdztwlydncf5exzmpj.streamlit.app/

## 7. Limitations & Next Steps

Simple linear model does not capture seasonal patterns or market changes

Future improvements: add moving average, or external factors like game releases

Consider adding net income or other financial metrics for comparison
