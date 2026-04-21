import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("NetEase Future Revenue Forecast Tool")

# Load data
df = pd.read_csv('netease_revenue.csv')

# Data cleaning
df['datadate'] = pd.to_datetime(df['datadate'])
df['revtq'] = pd.to_numeric(df['revtq'], errors='coerce')
df = df.dropna(subset=['revtq'])
df = df.sort_values('datadate').reset_index(drop=True)
df['quarter_num'] = range(1, len(df) + 1)

# Train model
X = df[['quarter_num']]
y = df['revtq']
model = LinearRegression()
model.fit(X, y)

# User selects number of quarters to predict
st.subheader("Select Forecast Period")
q_to_predict = st.slider("Number of quarters to forecast", 1, 8, 4)

# Predict
last_q = df['quarter_num'].max()
future_q = [[last_q + i] for i in range(1, q_to_predict + 1)]
predictions = model.predict(future_q)

# Display prediction results
st.subheader(f"Revenue Forecast for Next {q_to_predict} Quarter(s) (Million USD)")
result_df = pd.DataFrame({
    "Quarter": [f"Quarter {i}" for i in range(1, q_to_predict + 1)],
    "Forecast Revenue (Million USD)": [f"${pred:.0f}M" for pred in predictions]
})
st.table(result_df)

# Display chart
st.subheader("Historical Data & Forecast Trend")
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(df['quarter_num'], y, 'bo-', label='Historical Data', markersize=4)
ax.plot([last_q + i for i in range(1, q_to_predict + 1)], predictions, 'ro--', label='Forecast', markersize=8)
ax.set_xlabel('Quarter Number')
ax.set_ylabel('Quarterly Revenue (Million USD)')
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)

# Optional: show historical data
if st.checkbox("Show Historical Data"):
    st.subheader("Historical Quarterly Revenue Data")
    st.dataframe(df[['datadate', 'revtq']].tail(20))

# Display model info
st.subheader("Model Information")
st.write(f"R² Score: {model.score(X, y):.3f}")
st.write(f"Average quarterly growth: ${model.coef_[0]:.0f}M")