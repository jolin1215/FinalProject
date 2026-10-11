# FinalProject

A small data-visualization project exploring self-reported study habits from a
student survey. Built with **pandas** and **matplotlib / Plotly**, with a simple
**Streamlit** app for interactive charts.

## Contents

- `app.py` — Streamlit app that groups weekly study time into ranges and charts the
  number of students per range.
- `Untitled9.ipynb`, `Untitled9-6.ipynb` — exploratory notebooks (grouping study time
  and plotting counts by sex and by faculty).
- `活頁簿1.xlsx`, `活頁簿2.xlsx` — the survey data. Columns: biological sex
  (`生理性別`), weekly study hours (`每週讀書時間` / `平均一個星期讀書時間`) and faculty
  (`學院`). The data is anonymous and aggregate — it contains no names or identifiers.

## Run

```bash
pip install streamlit pandas matplotlib plotly openpyxl
streamlit run app.py
```

> `requirements.txt` also lists libraries left over from other experiments
> (e.g. `yfinance`, `backtesting`); the survey app itself only needs the packages above.
