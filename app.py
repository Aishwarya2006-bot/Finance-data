import streamlit as st
import pandas as pd
from analysis import analyze_data

st.set_page_config(
    page_title="Finance Data Analyzer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Finance Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload Finance CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    results = analyze_data(df)

    st.subheader("Statistical Summary")
    st.dataframe(results["summary"])

    st.subheader("Missing Values")
    st.dataframe(results["missing"])

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:

        selected_col = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        st.subheader(f"Distribution of {selected_col}")

        st.bar_chart(
            df[selected_col].value_counts().head(20)
        )

        st.subheader("Trend Chart")

        st.line_chart(df[selected_col])

        st.subheader("Correlation Matrix")

        corr = df[numeric_cols].corr()

        st.dataframe(corr)

else:
    st.info("Upload a CSV file to begin analysis.")
