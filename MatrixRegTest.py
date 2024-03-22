from polygon import RESTClient
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import math
import numpy as np
from datetime import datetime
from datetime import timedelta
from LinearRegTest import * 

index_symbol = "SPY"
index_slope = run(index_symbol, 30, 7, "hour", 1)
print(index_slope)
tickers = pd.read_csv("constituents.csv")
symbols = tickers.Symbol
compl_symbols, symbol_slopes, variance, week_slopes, index_slopes = ([] for i in range(5))
#finance = []
#communication = []
#health_care = []
#info_tech = []
#energy = []
#industrials = []
start_time = datetime.now()
for symbol in symbols:
    try:
        m, mean_diff = run(symbol, 30, 7, "day", 1)
        compl_symbols = [symbol]
        symbol_slopes += [m]
        variance += [mean_diff]
        week_slopes = run(symbol, 7, 0, "hour", 6)
        index_slopes += [index_slope]
        print(symbol)
    except:
        print("Error on {}: {}".format(symbol, OSError))
print((start_time - datetime.now()).strftime("%H:%M:%S"))


test = pd.DataFrame({'symbol': compl_symbols, 'index_slope': index_slopes, 'prev_slope': symbol_slopes, 'mean_diff': variance, 'week_slope': week_slopes})
#test = pd.DataFrame({"symbol": symbols "index_slope": index_slope, "prev_slope": [-10, 5, -3], "mean_diff": [5, 6, 1], "finance":[1, 0, 1], "communication":[1, 0, 1], "health_care": [1, 0, 1], "information_tech": [1, 0, 1],
#                                                  "energy": [1, 0, 1], "industrials": [1, 0, 1], "healthcare": [1, 0, 1], "real_estate": [1, 0, 1], 
#                                                  "utilities":[1, 0, 1],"materials":[1, 0, 1],"consumer_disc":[1, 0, 1],"consumer_staples":[1, 0, 1],"week_slope": [-1, 8, 3]})

print(test)


# stock array = slope of index fund for past month,  slope of past month, avgdiff between high and low vals, array(company types (true or false)), next week slope
# coefficent matrix will hold coefficients as follows: constant (b), slopes (m0 - m(3 + i)) where i is the number of company types 
class StockRegSlopePredictor:
    def __init__(self, stock_data, initial_coefficient_matrix, learning_rate, num_iterations):
        self.stock_array = stock_array
        self.coeff = initial_coefficient_matrix
        self.lr = learning_rate
        self.iterations = num_iterations
    
    def train(prediction_column):
        X = self.stock_data(-[prediction_column])
        Y = self.stock_data([prediction_column])
        new_coeff = self.coeff
        new_coeff = gradient_descent_runner(X, Y, new_coeff, self.lr, self.iterations)

    def gradient_descent_runner(X, Y, coeff, learning_rate, num_iterations):
        new_coeff = coeff
        for i in range(0, numiterations):
            new_coeff = gradient_step(X, Y, new_coeff, learning_rate)
        return new_coeff

    def gradient_step(X, Y, coeff, learning_rate):
        coeff_gradient = np.zeros((len(coeff), 1))
        N = float(len(X[1]))
        for i in range(0, int(N)):
            y_pred = np.dot(X, coeff_gradient)

            cost = (1/2*N) * np.sum(np.square(Y - y_pred))

            coeff_gradient_d = (1/m) * np.dot(X.T, y_pred - Y)
            coeff_gradient = coeff_gradient - (learning_rate * coeff_gradient_d)

        return coeff_gradient
