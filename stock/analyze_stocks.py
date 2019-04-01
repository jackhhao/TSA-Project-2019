from yahoo_fin.stock_info import *
import numpy as np
from datetime import date, timedelta
day = (date.today() - timedelta(10)).strftime("%d/%m/%Y")
mean = get_data(ticker="AAPL", start_date = day)["close"].mean()
stdev = np.std(get_data(ticker="AAPL", start_date = '03/05/2019')["close"])/mean
high = (1+stdev)*mean
print(high)
low = (1-stdev)*mean
print(low)
x = get_quote_table(stock ticker)["Avg. Volume"]

if x>17500000:
    if x > 25000000:
        z = 1
    else:
        z = 0.75
elif x<5000000:
    if x<1000000:
        z = 0.1
    else:
        z = 0.25
else:
    z = 0.5
print("A score will print out with 1 being the safest and 0.1 being the riskiest")
print(z)
