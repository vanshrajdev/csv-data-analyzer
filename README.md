# 📊 CSV Data Analyzer Dashboard

An interactive data analysis web application built with **Python**, **Pandas**, **Plotly**, and **Streamlit**.  
Upload any CSV file and instantly get statistics, visualizations, and insights — no coding required from the user.

---
## 🚀 Live Demo

[Open Live App](https://csv-data-analyzer-fysxywugv5r8arryfpk5fd.streamlit.app/)


---

## ✨ Features

- 📋 **Dataset Overview** — row count, column count, data types at a glance
- 🔴 **Data Quality Check** — missing value detection, duplicate row identification, completeness report
- 📊 **Statistical Summary** — auto-generated mean, median, std deviation, min/max for all numeric columns
- 📈 **Interactive Charts**
  - Histogram + Box Plot for distribution analysis
  - Bar Chart for categorical column frequency
  - Scatter Plot with trendline and optional color grouping
- 🔗 **Correlation Heatmap** — visualize relationships between numeric variables
- 🔍 **Column Explorer** — drill into any single column for detailed info
- ⬇️ **Download Cleaned CSV** — export null-removed dataset with one click

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core programming language |
| Pandas | Data loading, cleaning, and analysis |
| Plotly | Interactive charts and heatmaps |
| Streamlit | Web application framework |
| NumPy | Numerical operations |

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/csv-data-analyzer.git
cd csv-data-analyzer
```

**2. Install dependencies**
```bash
pip install streamlit pandas plotly numpy
```

**3. Run the application**
```bash
streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 📁 Project Structure

```
csv-data-analyzer/
│
├── app.py          # Main Streamlit application
├── README.md       # Project documentation
└── requirements.txt
```

---

## 📦 Requirements

Create a `requirements.txt` file with:
```
streamlit
pandas
plotly
numpy
```

---

## 📸 Screenshots
![Dashboard](Screenshot%202026-05-14%20232539.png)

![Dashboard](Screenshot%202026-05-14%20232706.png)

![Dashboard](Screenshot%202026-05-14%20232740.png)

> *(Add screenshots of your running app here after testing)*  
> In VS Code terminal: `Ctrl + Shift + S` to screenshot, or just use Windows Snipping Tool.

---

## 🧪 Sample Datasets to Test With

| Dataset | Source | Good for testing |
|---|---|---|
| Titanic | [Download](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv) | Mixed numeric + categorical |
| Iris | [Download](https://raw.githubusercontent.com/datasciencedojo/datasets/master/iris.csv) | Pure numeric, correlation heatmap |
| Netflix Titles | Kaggle | Categorical heavy |

---

## 💡 What I Learned

- End-to-end data pipeline: CSV ingestion → cleaning → EDA → visualization
- Building interactive web UIs using Streamlit without any frontend code
- Data quality assessment using Pandas (null detection, duplicate handling)
- Creating correlation matrices and statistical summaries programmatically
- Deploying Python data apps on Streamlit Cloud

---

## 🔮 Future Improvements

- [ ] Add ML model training directly from uploaded data
- [ ] Support Excel (.xlsx) file uploads
- [ ] Add AI-generated text insights using an LLM API
- [ ] Add export to PDF report feature

---

## 👤 Author

**Vansh Rajdev**  
B.E. ECE — University Institute of Engineering & Technology, Panjab University, Chandigarh  
📧 vanshrajdev06@gmail.com  
🔗 [LinkedIn](https://linkedin.com)  
🐙 [GitHub](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
