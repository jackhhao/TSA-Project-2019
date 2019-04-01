from yahoo_fin.stock_info import *
import numpy as np
from datetime import date, timedelta
day = (date.today() - timedelta(10)).strftime("%d/%m/%Y")
mean = get_data(ticker="AAPL", start_date = day)["close"].mean()
stdev = np.std(get_data(ticker="AAPL", start_date = '03/05/2019')["close"])/mean
high = (1+stdev)*mean
print("High: ", high)
low = (1-stdev)*mean
print("Low: ", low)

vol = get_quote_table(stock ticker)["Avg. Volume"]
volRisk = 0.5
if vol>17500000:
    if vol > 25000000:
        volRisk = 1
    else:
        volRisk = 0.75
elif vol<5000000:
    if vol<1000000:
        volRisk = 0.1
    else:
        volRisk = 0.25
print("A score will print out with 1 being the safest and 0.1 being the riskiest: ", volRisk)
