import streamlit as st
import pandas as pd
import plotly.express as px

from analysis import *

st.set_page_config(
    page_title="Finance Dashboard",
    layout="wide"
)

st.title("📈 Finance Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload Finance CSV File",
    type=["csv"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.success("CSV Uploaded Successfully")

    # -----------------------
    # Preview
    # -----------------------

    st.header("Dataset Preview")

    st.dataframe(df.head())

    # -----------------------
    # Basic Info
    # -----------------------

    info = get_basic_info(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", info["Rows"])
    col2.metric("Columns", info["Columns"])
    col3.metric("Missing", info["Missing Values"])
    col4.metric("Duplicates", info["Duplicates"])

    # -----------------------
    # Statistics
    # -----------------------

    st.header("Summary Statistics")

    st.dataframe(summary_stats(df))

    # -----------------------
    # Numeric Columns
    # -----------------------

    numeric_cols = list(
        df.select_dtypes(include="number").columns
    )

    if len(numeric_cols) > 0:

        amount_col = st.selectbox(
            "Select Financial Column",
            numeric_cols
        )

        metrics = financial_metrics(
            df,
            amount_col
        )

        st.header("Financial Metrics")

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Total", f"{metrics['Total']:.2f}")
        m2.metric("Average", f"{metrics['Average']:.2f}")
        m3.metric("Maximum", f"{metrics['Maximum']:.2f}")
        m4.metric("Minimum", f"{metrics['Minimum']:.2f}")

        # -----------------------
        # Histogram
        # -----------------------

        st.header("Distribution")

        fig = px.histogram(
            df,
            x=amount_col,
            nbins=30
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -----------------------
    # Monthly Trend
    # -----------------------

    st.header("Monthly Trend")

    date_candidates = df.columns

    date_col = st.selectbox(
        "Select Date Column",
        date_candidates
    )

    if len(numeric_cols) > 0:

        trend_col = st.selectbox(
            "Select Amount Column",
            numeric_cols,
            key="trend"
        )

        if st.button("Generate Trend"):

            monthly = monthly_analysis(
                df,
                date_col,
                trend_col
            )

            st.dataframe(monthly)

            fig2 = px.line(
                monthly,
                x=date_col,
                y=trend_col,
                markers=True,
                title="Monthly Financial Trend"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

    # -----------------------
    # Download Data
    # -----------------------

    st.header("Download")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="processed_data.csv",
        mime="text/csv"
    )
