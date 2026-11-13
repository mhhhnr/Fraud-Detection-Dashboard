FRAUD DETECTION DASHBOARD (burgundy edition)
Run: double-click serve.bat (or: python -m http.server 8000) and open http://localhost:8000
Do NOT double-click index.html: the browser blocks loading the data files that way.
Pages: Overview (charts), Score only, Technical (SHAP), Explanation (plain language). Search any TransactionID at the top.
Links look like index.html#/B/3516550 . D3 loads from cdnjs, so an internet connection is needed for the charts.
Overview charts use the held-out test predictions from the teammate's models (XGBoost, Random Forest, Logistic Regression).
