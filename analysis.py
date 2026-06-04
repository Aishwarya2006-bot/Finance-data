import pandas as pd


def load_data(file):
    return pd.read_csv(file)


def get_basic_info(df):

    info = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": df.isnull().sum().sum(),
        "Duplicates": df.duplicated().sum()
    }

    return info


def summary_stats(df):

    return df.describe()


def monthly_analysis(df, date_col, amount_col):

    df[date_col] = pd.to_datetime(df[date_col])

    monthly = (
        df.groupby(df[date_col].dt.to_period("M"))
        [amount_col]
        .sum()
        .reset_index()
    )

    monthly[date_col] = monthly[date_col].astype(str)

    return monthly


def financial_metrics(df, amount_col):

    total = df[amount_col].sum()

    average = df[amount_col].mean()

    maximum = df[amount_col].max()

    minimum = df[amount_col].min()

    return {
        "Total": total,
        "Average": average,
        "Maximum": maximum,
        "Minimum": minimum
    }
