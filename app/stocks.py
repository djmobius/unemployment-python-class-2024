# ENV VARS

from app.alpha import API_KEY

# STOCK SELECTION

symbol = input("Please input a symbol (e.g. 'NFLX'): ")
print("SYMBOL:", symbol)

# REPORT

from pandas import read_csv

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv"

df = read_csv(request_url)

print(df.columns)
print(len(df))
df.head()

# Challenge A
#
# What is the most recent adjusted closing price? And the corresponding date?
# Display the price formatted as USD, with dollar sign and two decimal places.

print("-------------------------")
print("LATEST CLOSING PRICE:")
first_row = df.iloc[0]
#print(first_row)
print(f"${first_row['adjusted_close']}", "as of", first_row["timestamp"])


# Challenge B
#
# What is the average, median, min, and max adjusted closing price
# (over the latest 100 available days only)?

recent_df = df.iloc[0:100] # use slicing or df.head(100)
print(len(recent_df))

print("-------------------------")
print("RECENT STATS...")
print(f"MEAN PRICE: ${recent_df['adjusted_close'].mean()}")
print(f"MEDIAN PRICE: ${recent_df['adjusted_close'].median()}")
print(f"MIN PRICE: ${recent_df['adjusted_close'].min()}")
print(f"MAX PRICE: ${recent_df['adjusted_close'].max()}")
# quantiles, for fun :-)
print(f"75TH PERCENTILE: ${recent_df['adjusted_close'].quantile(.75).round(2)}")
print(f"25TH PERCENTILE: ${recent_df['adjusted_close'].quantile(.25).round(2)}")

# Challenge C
#
# Plot a line chart of adjusted closing prices over time (all time).

from plotly.express import line

fig = line(x=df["timestamp"], y=df["adjusted_close"],
            title=f"Stock Prices ({symbol})",
           labels= {"x": "Date", "y": "Stock Price ($)"})
fig.show()