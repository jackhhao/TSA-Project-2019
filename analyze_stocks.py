import paralleldots
import getURLs
import numpy as np

from datetime import date, timedelta
from newspaper import Article
from yahoo_fin.stock_info import *

paralleldots.set_api_key("VkuigAku4meDwQPFy0uHHxRZilBTSTQuu9PEmLMAOas")
lang_code = "en"

def getVolume(t):
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
    return volRisk

def getHL(t, td, opt):
    day = (date.today() - timedelta(td)).strftime("%d/%m/%Y")
    mean = get_data(ticker=t, start_date = day)["close"].mean()
    stdev = np.std(get_data(ticker=t, start_date = day)["close"])/mean
    high = (1+stdev)*mean
    low = (1-stdev)*mean
    if(opt == "High"):
        return high
    elif(opt == "Low"):
        return low

def sentiment(ticker):
    FYPapers = getURLs.urls(ticker)
    count = 0
    score = 0
    for url in FYPapers:
        article = Article(url)
        count += 1
        article.download()
        article.parse()
        text = article.text
        response = paralleldots.sentiment(text, lang_code)["sentiment"]
        score += ((response["positive"] - response["negative"])*(1-response["neutral"]))
    return (score/count)

def getVolatility(ticker, td):
    day = (date.today() - timedelta(td)).strftime("%d/%m/%Y")
    L = [i for i in get_data(ticker=ticker, start_date = day)["close"]]
    c=0
    L2 = [abs(((L[c] - i)/L[c]) * 100) for i in get_data(ticker=ticker, start_date = day)["open"]]
    c+=1
    avgVolatility = sum(L2)/len(L2)
    v = 0.1
    if avgVolatility<1:
        v = 1
    elif avgVolatility < 3:
        v = 0.75;
    elif avgVolatility<5:
        v = 0.5;
    return(v)
