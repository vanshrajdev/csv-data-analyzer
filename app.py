import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CSV Data Analyzer",
    page_icon="📊",
    layout="wide"
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("📊 CSV Data Analyzer Dashboard")
st.markdown("Upload any CSV file and instantly get statistics, charts, and insights.")
st.divider()

# ── File Upload ───────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is None:
    st.info("👆 Upload a CSV file to get started. No CSV? Download one from Kaggle.com")

    # Show a sample so the app doesn't look empty
    st.subheader("Example: What you'll see after upload")
    sample = pd.DataFrame({
        "Name":   ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Age":    [24, 30, 22, 28, 35],
        "Score":  [88, 72, 95, 81, 67],
        "City":   ["Delhi", "Mumbai", "Chandigarh", "Pune", "Jaipur"]
    })
    st.dataframe(sample, use_container_width=True)
    st.stop()

# ── Load Data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Could not read file: {e}")
        return None

df = load_data(uploaded_file)

if df is None:
    st.stop()

# ── Separate column types ─────────────────────────────────────────────────────
numeric_cols   = df.select_dtypes(include=np.number).columns.tolist()
categoric_cols = df.select_dtypes(include="object").columns.tolist()

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — Dataset Overview
# ══════════════════════════════════════════════════════════════════════════════
st.header("1️⃣  Dataset Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("📋 Total Rows",    f"{df.shape[0]:,}")
col2.metric("📌 Total Columns", f"{df.shape[1]}")
col3.metric("🔢 Numeric Cols",  f"{len(numeric_cols)}")
col4.metric("🔤 Text Cols",     f"{len(categoric_cols)}")

st.subheader("Raw Data Preview")
n_rows = st.slider("Rows to preview", 5, min(100, len(df)), 10)
st.dataframe(df.head(n_rows), use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — Data Quality
# ══════════════════════════════════════════════════════════════════════════════
st.divider()
st.header("2️⃣  Data Quality Check")

null_counts  = df.isnull().sum()
null_percent = (null_counts / len(df) * 100).round(2)
duplicates   = df.duplicated().sum()

quality_df = pd.DataFrame({
    "Column":        df.columns,
    "Data Type":     df.dtypes.astype(str).values,
    "Missing Values": null_counts.values,
    "Missing %":     null_percent.values,
    "Unique Values": [df[c].nunique() for c in df.columns]
})

st.dataframe(quality_df, use_container_width=True)

qcol1, qcol2 = st.columns(2)
qcol1.metric("🔴 Duplicate Rows", f"{duplicates}")
qcol2.metric("✅ Complete Rows",  f"{len(df) - duplicates:,}")

if duplicates > 0:
    if st.button("🗑️ Drop Duplicate Rows"):
        df = df.drop_duplicates()
        st.success(f"Removed {duplicates} duplicate rows. Dataset now has {len(df):,} rows.")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — Statistical Summary
# ══════════════════════════════════════════════════════════════════════════════
if numeric_cols:
    st.divider()
    st.header("3️⃣  Statistical Summary")
    st.dataframe(df[numeric_cols].describe().round(3), use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — Charts
# ══════════════════════════════════════════════════════════════════════════════
st.divider()
st.header("4️⃣  Data Visualisation")

tab1, tab2, tab3 = st.tabs(["📈 Distribution", "📊 Category Counts", "🔗 Scatter Plot"])

# Tab 1 — Histogram
with tab1:
    if numeric_cols:
        col = st.selectbox("Select numeric column", numeric_cols, key="hist_col")
        fig = px.histogram(
            df, x=col, nbins=30,
            title=f"Distribution of {col}",
            color_discrete_sequence=["#4F8EF7"]
        )
        fig.update_layout(bargap=0.05)
        st.plotly_chart(fig, use_container_width=True)

        # Box plot below
        fig2 = px.box(df, y=col, title=f"Box Plot — {col}",
                      color_discrete_sequence=["#4F8EF7"])
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("No numeric columns found in this dataset.")

# Tab 2 — Bar chart for categorical
with tab2:
    if categoric_cols:
        cat_col = st.selectbox("Select category column", categoric_cols, key="bar_col")
        top_n   = st.slider("Show top N values", 5, 30, 10, key="topn")
        counts  = df[cat_col].value_counts().head(top_n).reset_index()
        counts.columns = [cat_col, "Count"]
        fig3 = px.bar(
            counts, x=cat_col, y="Count",
            title=f"Top {top_n} values in '{cat_col}'",
            color="Count",
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("No categorical columns found.")

# Tab 3 — Scatter
with tab3:
    if len(numeric_cols) >= 2:
        sc1, sc2 = st.columns(2)
        x_col = sc1.selectbox("X axis", numeric_cols, index=0, key="sx")
        y_col = sc2.selectbox("Y axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0, key="sy")

        color_col = None
        if categoric_cols:
            color_col = st.selectbox("Color by (optional)", ["None"] + categoric_cols, key="sc_color")
            if color_col == "None":
                color_col = None

        fig4 = px.scatter(
            df, x=x_col, y=y_col,
            color=color_col,
            title=f"{x_col} vs {y_col}",
            trendline="ols",
            opacity=0.7
        )
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.warning("Need at least 2 numeric columns for scatter plot.")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — Correlation Heatmap
# ══════════════════════════════════════════════════════════════════════════════
if len(numeric_cols) >= 2:
    st.divider()
    st.header("5️⃣  Correlation Heatmap")
    st.caption("Shows how strongly pairs of numeric columns are related. Values close to 1 or -1 = strong correlation.")

    corr  = df[numeric_cols].corr().round(2)
    fig5  = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1,
        title="Correlation Matrix"
    )
    fig5.update_layout(height=500)
    st.plotly_chart(fig5, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — Column Explorer
# ══════════════════════════════════════════════════════════════════════════════
st.divider()
st.header("6️⃣  Column Explorer")
explore_col = st.selectbox("Pick any column to explore", df.columns.tolist())

exp1, exp2 = st.columns(2)
with exp1:
    st.markdown(f"**Data Type:** `{df[explore_col].dtype}`")
    st.markdown(f"**Unique Values:** {df[explore_col].nunique()}")
    st.markdown(f"**Missing Values:** {df[explore_col].isnull().sum()}")
with exp2:
    st.markdown("**Sample Values:**")
    st.write(df[explore_col].dropna().sample(min(5, len(df))).values)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 7 — Download Cleaned CSV
# ══════════════════════════════════════════════════════════════════════════════
st.divider()
st.header("7️⃣  Download Cleaned Data")
cleaned = df.dropna()
st.write(f"Cleaned dataset: {len(cleaned):,} rows (nulls removed)")

csv_bytes = cleaned.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download Cleaned CSV",
    data=csv_bytes,
    file_name="cleaned_data.csv",
    mime="text/csv"
)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built with Python · Pandas · Plotly · Streamlit")