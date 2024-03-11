import yfinance as yf #Python library that allows us to download financial data from Yahoo Finance
import pandas as pd

#dataF is a pandas DataFrame (basically a table of data)
#keys in dataF = column names of the DataFrame
#row names are date and time info
dataF = yf.download("EURUSD=X", start="2024-2-1", end="2024-3-1", interval='60m') #EUR => USD conversion data

def signal_generator(df): #generates signal for every two rows ( two sequential hours) of data in dataF
    open = df.Open.iloc[-1] #.Open gives the returns data info and open value; slicing [-1] just gives open value for second hour in df
    close = df.Close.iloc[-1] #iloc slices from appropriate structure
    previous_open = df.Open.iloc[-2] #first hour in df
    previous_close = df.Close.iloc[-2]
    # Bearish Pattern: downward trend in prices
    if (open>close and previous_open<previous_close and close<previous_open and open>=previous_close):
        return 1
    # Bullish Pattern: upward trend in prices
    elif (open<close and previous_open>previous_close and close>previous_open and open<=previous_close):
        return 2
    # No clear pattern
    else:
        return 0

signals = []
signals.append(0) #no clear pattern for first two hours
for i in range(1,len(dataF)): #going through the hour data
    df = dataF[i-1:i+1] 
    #print(df.Open) #prints both open values contained in df
    signals.append(signal_generator(df)) #collecting signal values for each two hour set of dataF
dataF["signal"] = signals
print(dataF.signal.value_counts()) #returns a pandas Series object containing counts of unique values in descending order for key signal
#a pandas Series object is like a column in a table: it is a 1D array that can hold data of any type


