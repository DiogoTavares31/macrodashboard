# 📊 Macro & Market Intelligence Dashboard

This project is a data-driven macroeconomic and market monitoring dashboard built with **Streamlit**. It aggregates real-time macro indicators, financial market data, and financial news headlines into one clean and interactive interface.

---

## 🔧 Key Features

- **Macroeconomic Data Fetching**:
  - GDP growth, unemployment rate, inflation (CPI), and interest rates from the **FRED API**.
  - Real-time computation of economic models for scenario analysis.

- **Market Data Monitoring**:
  - Price data for major assets: S&P 500 (SPY), Gold (GLD), Oil (USO), and Wheat (WEAT) using **yFinance**.
  - Fear & Greed Index sentiment gauge.

- **News Aggregation & Summarization**:
  - Financial and macroeconomic news pulled via **RSS feeds**.
  - Automatic text summarization using transformer-based **NLP models** (e.g., BART or similar).
  - Clean interface for viewing concise, digestible summaries of the latest headlines.

- **Streamlit Frontend**:
  - Interactive economic modeling (interest vs. inflation).
  - Simple, modular design with expandable panels and visualization support.

---

## 📌 Example Use Cases

- Quickly check macroeconomic conditions and market sentiment.
- Monitor market prices and economic indicators in one place.
- Get summarized headlines for efficient market briefings.
- Use interactive models to explore inflation vs. interest rate scenarios.

---

## To Do

- Improve plot visuals.
- Include asset correlation heatmaps.
- Build alerting systems for economic threshold triggers.

---

## 📷 Screenshots

*To be added soon.*

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/DiogoTavares31/macrodashboard.git
cd macro-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_dashboard.py
