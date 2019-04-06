from yahoo_fin.stock_info import *
import numpy as np
from datetime import date, timedelta
import sentiment_analysis
t = "AAPL"
td = 10
day = (date.today() - timedelta(td)).strftime("%d/%m/%Y")
mean = get_data(ticker=t, start_date = day)["close"].mean()
stdev = np.std(get_data(ticker=t, start_date = '03/05/2019')["close"])/mean
high = (1+stdev)*mean
print("High: ", high)
low = (1-stdev)*mean
print("Low: ", low)

vol = get_quote_table(t)["Avg. Volume"]
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

print("A general sentiment indicator will be printed out")
print("Positive values indicate that there is positive market sentiment regarding the stock's performance")
print("Negative values indicate that there is negative market sentiment regarding the stock's performance")
Sentiment_Score = getSentiment(main(url))
if Sentiment_Score <0:
    print("General market sentiment strongly indicates against buying this stock")
elif Sentiment_Score >0:
    print("General market sentiment strongly is in favor of purchasing this stock")



