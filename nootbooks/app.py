import streamlit as st
import pandas as pd
import plotly.express as px

from analysis import (
    basic_analysis,
    calculate_returns,
    calculate_metrics
)

st.set_page_config(
    page_title="Finance Data Analyzer",
    layout="wide"
)

st.title("📈 Finance CSV Analyzer")

uploaded_file = st.file_uploader(
    "Upload Finance CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    st.subheader("Basic Statistics")

    summary, missing = basic_analysis(df)

    st.dataframe(summary)

    st.subheader("Missing Values")

    st.dataframe(missing)

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:

        st.subheader("Column Visualization")

        selected_col = st.selectbox(
            "Choose Numeric Column",
            numeric_columns
        )

        fig = px.line(
            df,
            y=selected_col,
            title=f"{selected_col} Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Finance Section

    st.subheader("Finance Analysis")

    price_columns = st.selectbox(
        "Select Price Column",
        numeric_columns
    )

    if st.button("Run Finance Analysis"):

        finance_df = calculate_returns(
            df,
            price_columns
        )

        metrics = calculate_metrics(finance_df)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Return",
            f"{metrics['Average Return']:.4%}"
        )

        col2.metric(
            "Volatility",
            f"{metrics['Volatility']:.4%}"
        )

        col3.metric(
            "Cumulative Return",
            f"{metrics['Cumulative Return']:.2%}"
        )

        fig = px.line(
            finance_df,
            y="Return",
            title="Daily Returns"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Processed Data")

        st.dataframe(finance_df.head())
