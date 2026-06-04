import pandas as pd
import numpy as np

def basic_analysis(df):

    summary = df.describe()

    missing_values = df.isnull().sum()

    return summary, missing_values


def calculate_returns(df, price_column):

    df = df.copy()

    df["Return"] = df[price_column].pct_change()

    return df


def calculate_metrics(df, return_column="Return"):

    avg_return = df[return_column].mean()

    volatility = df[return_column].std()

    cumulative_return = (
        (1 + df[return_column]).cumprod().iloc[-1] - 1
    )

    return {
        "Average Return": avg_return,
        "Volatility": volatility,
        "Cumulative Return": cumulative_return
    }
