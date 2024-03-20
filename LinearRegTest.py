from polygon import RESTClient
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import math
import numpy as np
from datetime import datetime
from datetime import timedelta


def get_data(timeSpanName, timeValue, timeMulti, ticker):
    client = RESTClient(api_key="h8IoGYiQLCNjfJfU7je02JpmLrk4SJF9")


    aggs = []
    closeVals = [] #close values for each hour mark, top value of each hour bar
    hourMarks = [] #x values for visualization
    #only free Polygon data call lmao
    today = datetime.now().strftime('%Y-%m-%d') #makes string of today
    prior = (datetime.now() - timedelta(timeValue)).strftime('%Y-%m-%d') #makes string of starting day
    for a in client.list_aggs(ticker=ticker, multiplier=timeMulti, timespan=timeSpanName, from_=prior, to=today, limit=50000):
       aggs.append(a)
    for i, a in enumerate(aggs):
        closeVals += [a.close]
        hourMarks += [i]
    print(len(closeVals))
    return [closeVals, hourMarks]


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



def gradient_descent_runner(points, starting_b, starting_m, learningrate, numiterations):
    b = starting_b
    m = starting_m

    for i in range(0, numiterations):
        m, b = gradient_step(b, m, points, learningrate)
        #print(calc_error(m, b, points))
    return [m,b]

def run():
    timeValue = 30
    timeSpanName = "hour"
    timeMulti = 12
    ticker = "AAPL"
    points = get_data(timeSpanName, timeValue, timeMulti, ticker)
    b = points[0][0]
    m = 0
    
    learningrate = 0.006/(timeValue**2)
    iterations = int(5000*np.sqrt(timeValue))
    

    m,b = gradient_descent_runner(points, b, m, learningrate, iterations)
    print(calc_error(m, b, points))
    x = np.array(points[1])
    y = m * x + b

    plt.plot(x, y)
    plt.scatter(points[1], points[0], 1)
    plt.show()

if __name__ == '__main__':
    run()