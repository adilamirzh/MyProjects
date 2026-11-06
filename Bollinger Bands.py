import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

symbols = ["SPY"] #"AAPL", "MSFT", "NVDA", "GOOGL"

start_date = "2026-07-22"
end_date = "2026-11-03"
window=20

def norm_data(df):
    return df/df.iloc[0]

df = yf.download(
    tickers=symbols,
    start=start_date,
    end=end_date,
    interval="1d"
)["Close"]

# df=norm_data(df)


def bollinger_bands(df):
    ax = df.plot(title='SPY Rolling Mean', label='SPY', figsize=(12, 6))

    rm_SPY = df.rolling(window).mean()
    rm_SPY.plot(label='Rolling Mean (20 days)', linestyle="dashed", ax=ax)

    std_SPY = df.rolling(window).std()

    upper_band = rm_SPY + 2 * std_SPY
    lower_band = rm_SPY - 2 * std_SPY
    condition= upper_band<df
    selected=upper_band[condition]

    condition2 = lower_band > df
    selected2 = lower_band[condition2]

    upper_band.plot(label='Upper Band',color="green", ax=ax)
    lower_band.plot(label='Lower Band', color="red", ax=ax)


    ax.set_xlabel('Date')
    ax.set_ylabel('Price ($)')

    ax.scatter(selected.index, selected.values, color="red", marker="x", zorder=5)
    ax.scatter(selected2.index, selected2.values, color="green", marker="x", zorder=5)
    ax.legend(loc='upper left')



    plt.show()

bollinger_bands(df)