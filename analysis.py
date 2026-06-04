import pandas as pd


def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df


def basic_info(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum()
    }


def numeric_summary(df):
    return df.describe()


def correlation_matrix(df):
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.corr()


def monthly_summary(df, date_col, amount_col):
    df[date_col] = pd.to_datetime(df[date_col])

    monthly = (
        df.groupby(df[date_col].dt.to_period("M"))[amount_col]
        .sum()
        .reset_index()
    )

    monthly[date_col] = monthly[date_col].astype(str)

    return monthly
