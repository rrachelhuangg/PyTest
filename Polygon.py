from polygon import RESTClient
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import math
from datetime import datetime
from datetime import timedelta

client = RESTClient(api_key="h8IoGYiQLCNjfJfU7je02JpmLrk4SJF9")

ticker = "AAPL"

aggs = [] #values for Apple stock by hour in a 48 hour time span from 3/4/24 to 3/5/24
openVals = [] #open values for each hour mark, bottom value of each hour bar
closeVals = [] #close values for each hour mark, top value of each hour bar
highs = [] #high values for each hour mark
lows = [] #low values for each hour mark
hourMarks = [] #x values for visualization
#only free Polygon data call lmao
today = datetime.now().strftime('%Y-%m-%d') #makes string of today
prior = (datetime.now() - timedelta(7)).strftime('%Y-%m-%d') #makes string of starting day
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="hour", from_=prior, to=today, limit=50000):
    aggs.append(a)
for i, a in enumerate(aggs):
    highs += [a.high]
    lows += [a.low]
    openVals += [a.open]
    closeVals += [a.close]
    hourMarks += [i]
#creating a visualization for the data (Japanese candlestick chart)
stock_prices = pd.DataFrame({'open': openVals, 'close': closeVals, 'high': highs,'low': lows},index=hourMarks)
up = stock_prices[stock_prices.close >= stock_prices.open]
down = stock_prices[stock_prices.close < stock_prices.open]
width = 0.5
width2 = 0.1
col1 = "red"
col2 = "green"
plt.bar(up.index, up.close-up.open, width, bottom=up.open, color=col2) # thick bar (close-open)
plt.bar(up.index, up.high-up.close, width2, bottom=up.close, color=col2) # top thin bar (high)
plt.bar(up.index, up.low-up.open, width2, bottom=up.open, color=col2) # bot thin bar (low)
plt.bar(down.index, down.close-down.open, width, bottom=down.open, color=col1) # thick bar (open-close)
plt.bar(down.index, down.high-down.open, width2, bottom=down.open, color=col1) # top thin bar (high)
plt.bar(down.index, down.low-down.close, width2, bottom=down.close, color=col1) # bot thin bar (low)

first = stock_prices[:-1]
last = stock_prices[1:]
plt.plot(first.index, first.close, last.index, last.close, color="black")

plt.

plt.title("Apple Stock From %s - %s" % (prior, today))
plt.xlabel("Number of Hours Into the Week Time Span")
plt.xlim(0, len(stock_prices))
plt.ylabel("Stock Value in USD")
plt.ylim(min(lows)-0.01*min(lows), max(highs) + 0.01*max(highs)) #setting the bounds for the y-axis
# plt.autofocus()
mpld3.show()

