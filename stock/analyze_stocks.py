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