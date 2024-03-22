from polygon import RESTClient
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import math
import numpy as np
from datetime import datetime
from datetime import timedelta


def get_data(timeSpanName, timeValue, end_time, timeMulti, ticker):
    client = RESTClient(api_key="h8IoGYiQLCNjfJfU7je02JpmLrk4SJF9")


    aggs = []
    closeVals = [] #close values for each hour mark, top value of each hour bar
    hourMarks = [] #x values for visualization
    highs = []
    lows = []
    #only free Polygon data call lmao
    end_day = datetime.now() - timedelta(end_time)
    end = (end_day).strftime('%Y-%m-%d') #makes string of today
    start = (end_day - timedelta(timeValue)).strftime('%Y-%m-%d') #makes string of starting day
    for a in client.list_aggs(ticker=ticker, multiplier=timeMulti, timespan=timeSpanName, from_=start, to=end, limit=50000):
       aggs.append(a)
    for i, a in enumerate(aggs):
        closeVals += [a.close]
        hourMarks += [i]
        highs += [a.high]
        lows += [a.low]
    #print(len(closeVals))
    return [closeVals, hourMarks], [highs, lows]


def calc_error(m, b, points):
    totalError = 0
    for i in range(0, len(points[1])):
        x = points[1][i]
        y = points[0][i]
        totalError += (y - (m*x + b))**2
    return totalError/ float(len(points[1]))

def gradient_step(b_current, m_current, points, learningrate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points[1]))
    for i in range(0, len(points[1])):
        x = points[1][i]
        y = points[0][i]
        b_gradient += -(2/N) * (y - (m_current*x + b_current))
        m_gradient += -(2/N) * x * (y - (m_current*x + b_current))
    new_b = b_current - (b_gradient * learningrate)
    new_m = m_current - (m_gradient * learningrate)
    return [new_m, new_b]

def mean_diff_calc(var_data):
    total_diff = 0
    N = float(len(var_data[1]))
    for i in range(0, len(var_data[1])):
        total_diff += var_data[0][i] - var_data[1][i]
    return total_diff / N

def gradient_descent_runner(points, starting_b, starting_m, learningrate, numiterations):
    b = starting_b
    m = starting_m

    for i in range(0, numiterations):
        m, b = gradient_step(b, m, points, learningrate)
        #print(calc_error(m, b, points))
    return [m,b]

def run(ticker, start_time, end_time, timespan, timeMulti):
    timeValue = start_time - end_time
    timeSpanName = "hour"
    timeMulti = 12
    ticker = ticker
    points, var_data = get_data(timeSpanName, timeValue, end_time, timeMulti, ticker)
    b = points[0][0]
    m = 0
    
    learningrate = 0.006/(timeValue**2)
    iterations = int(5000*np.sqrt(timeValue))

    m,b = gradient_descent_runner(points, b, m, learningrate, iterations)
    #print(calc_error(m, b, points))
    x = np.array(points[1])
    y = m * x + b

    mean_diff = mean_diff_calc(var_data)
    # print(m)
    return m, mean_diff

if __name__ == '__main__':
    run('ON', 30, 7, "day", 1)
    # 'NOC' 'NUE' 'ON' 'OKE' 'RTX'