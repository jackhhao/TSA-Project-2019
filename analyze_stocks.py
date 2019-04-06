import paralleldots
import getURLs
import numpy as np
import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from datetime import date, timedelta
from newspaper import Article
from yahoo_fin.stock_info import *
from os import environ

paralleldots.set_api_key("VkuigAku4meDwQPFy0uHHxRZilBTSTQuu9PEmLMAOas")
lang_code = "en"
environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./TSA-2019-734637019630.json"
client = language.LanguageServiceClient()

def getVolume(t):
    '''
    try:
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
    except:
        return 0
        '''
    return get_quote_table(t)["Avg. Volume"]


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

def sentimentArticles(ticker):
    FYPapers = getURLs.urls(ticker)
    count = 0
    score = 0
    magnitude = 0
    for url in FYPapers:
        article = Article(url)
        count += 1
        article.download()
        try:
            article.parse()
            document = types.Document(
                content=article.text,
                type=enums.Document.Type.PLAIN_TEXT
            )
            annotations = client.analyze_sentiment(document=document)
            score += annotations.document_sentiment.score
            magnitude += annotations.document_sentiment.magnitude
        except:
            pass
    try:
        return score/count, magnitude/count
    except:
        return -1, -1

    #print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))


def getVolatility(ticker, td):
    '''
    day = (date.today() - timedelta(td)).strftime("%d/%m/%Y")
    try:
        L = [i for i in get_data(ticker=ticker, start_date = day)["close"]]
    except:
        return -100
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
    '''
    return avgVolatility

'''
import sys
import csv
import datetime
import re

import pandas as pd
import requests

def get_google_finance_intraday(ticker, exchange, period=60, days=1):
    """
    Retrieve intraday stock data from Google Finance.
    Parameters
    ----------
    ticker : str
        Company ticker symbol
    exchange : str
        Exchange of ticker
    period : int
        Interval between stock values in seconds.
    days : int
        Number of days of data to retrieve.
    Returns
    -------
    df : pandas.DataFrame
        DataFrame containing the opening price, high price, low price,
        closing price, and volume. The index contains the times associated with
        the retrieved price values.
    """

    uri = 'https://www.google.com/finance/getprices' \
          '?i={period}&p={days}d&f=d,o,h,l,c,v&q={ticker}&x={exchange}'.format(ticker=ticker,
                                                                          period=period,
                                                                          days=days,
                                                                          exchange=exchange)
    page = requests.get(uri)
    reader = csv.reader(page.content.splitlines())
    columns = ['Close', 'High', 'Low', 'Open', 'Volume']
    rows = []
    times = []
    for row in reader:
        if re.match('^[a\d]', row[0]):
            if row[0].startswith('a'):
                start = datetime.datetime.fromtimestamp(int(row[0][1:]))
                times.append(start)
            else:
                times.append(start+datetime.timedelta(seconds=period*int(row[0])))
            rows.append(map(float, row[1:]))
    if len(rows):
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'),
                            columns=columns)
    else:
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'))
'''
