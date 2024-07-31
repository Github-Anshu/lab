import plotly.express as px
import pandas as pd

def time_series():
    dates = pd.date_range(start='2021-01-01', periods=100)
    data = np.random.randn(100).cumsum()
    df = pd.DataFrame({'Date': dates, 'Value': data})

    fig = px.line(df, x='Date', y='Value', title='ANSHU GUPTA 1BI21CS020 Time Series Example')
    fig.show()

# Run the time series plot
time_series()
