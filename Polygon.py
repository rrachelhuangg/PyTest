from polygon import RESTClient

<<<<<<< HEAD
client = RESTClient()
=======
client = RESTClient(api_key="h8IoGYiQLCNjfJfU7je02JpmLrk4SJF9")
>>>>>>> 4156c5522612c23c5c773aedb1a51e56644ac641

ticker = "AAPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)

<<<<<<< HEAD
print(aggs)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)

# List Trades
trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
for trade in trades:
    print(trade)

# Get Last Quote
quote = client.get_last_quote(ticker=ticker)
print(quote)

# List Quotes
quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
for quote in quotes:
    print(quote)
=======
print(aggs)
>>>>>>> 4156c5522612c23c5c773aedb1a51e56644ac641
