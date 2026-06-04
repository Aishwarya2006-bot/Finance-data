import plotly.express as px


def line_chart(df, x_col, y_col):
    fig = px.line(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} Trend"
    )
    return fig


def bar_chart(df, x_col, y_col):
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} Analysis"
    )
    return fig


def pie_chart(df, names_col, values_col):
    fig = px.pie(
        df,
        names=names_col,
        values=values_col
    )
    return fig


def histogram(df, column):
    fig = px.histogram(
        df,
        x=column,
        nbins=30
    )
    return fig
