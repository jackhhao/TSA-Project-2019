import stock.getFY as getFY
import argparse
import sys
import csv
import datetime
import re
import requests
import pandas as pd
import numpy as np

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from datetime import date, timedelta
from newspaper import Article
from yahoo_fin.stock_info import *
from os import environ

lang_code = "en"
environ["GOOGLE_APPLICATION_CREDENTIALS"] = "assets/TSA-2019-734637019630.json"
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
    return get_quote_table(t)["Volume"]

def getHL(t, td, opt):
    day = (date.today() - timedelta(td)).strftime("%m/%d/%y")
    try:
        mean = get_data(ticker=t, start_date = day)["close"].mean()
        stdev = np.std(get_data(ticker=t, start_date = day)["close"])/mean
        high = (1+stdev)*mean
        low = (1-stdev)*mean
        if(opt == "High"):
            return high
        elif(opt == "Low"):
            return low
    except:
        return None
def sentimentArticles(ticker):
    FYPapers = getFY.urls(ticker)
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
    except ZeroDivisionError:
        return None, None

def sentimentConvos(ticker):
    FYConvos = getFY.convos(ticker)
    count = 0
    score = 0
    magnitude = 0
    for convo in FYConvos:
        count+=1
        try:
            document = types.Document(
                content=convo,
                type=enums.Document.Type.PLAIN_TEXT
            )
            annotations = client.analyze_sentiment(document=document)
            score += annotations.document_sentiment.score
            magnitude += annotations.document_sentiment.magnitude
        except:
            pass
    try:
        return score/count, magnitude/count
    except ZeroDivisionError:
        return None, None

def getVolatility(ticker, td):
    day = (date.today() - timedelta(td)).strftime("%m/%d/%y")
    L = [i for i in get_data(ticker = ticker, start_date = day)["close"]]
    L2 = []
    count = 0
    for i in get_data(ticker=ticker, start_date = day)["close"]:
        L.append(i)
    for i in get_data(ticker=ticker, start_date = day)["open"]:
        L2.append(abs(((L[count] - i)/L[count]) * 100))
        count+=1
    avgVolatility = sum(L2)/len(L2)
    return avgVolatility

def getActualVolatility(str, td):
    day = (date.today() - timedelta(td)).strftime("%m/%d/%y")
    L = []
    L2 = []
    count = 0
    for i in get_data(ticker=str, start_date = day)["close"]:
        L.append(i)
    for i in get_data(ticker=str, start_date = day)["open"]:
        L2.append(((L[count] - i)/L[count]) * 100)
        count+=1
    return sum(L2)

def getBeta(t):
    try:
        return get_quote_table(t)["Beta (3Y Monthly)"]
    except:
        return None

def getCurrentPrice(t):
    try:
        return get_live_price(t)
    except:
        return None

def searchHL(x, lowPrices, highPrices):
    for i in lowPrices:
        if i == x:
            return 1
    for i in highPrices:
        if i == x:
            return -1

def getFreq(ticker, td):
    day = (date.today() - timedelta(td)).strftime("%m/%d/%y")
    highPrices = [i for i in get_data(ticker = ticker, start_date=day)["high"]]
    lowPrices = [i for i in get_data(ticker = ticker, start_date = day)["low"]]
    allPrices = highPrices + lowPrices
    highPrices.sort()
    lowPrices.sort()
    allPrices.sort()
    count = 0
    frequency = 0
    lowFreq = 0
    highFreq = 0
    for price in allPrices:
        count += searchHL(price, lowPrices, highPrices)
        if count > frequency:
            lowFreq  = price
        if searchHL(price, lowPrices, highPrices) == -1:
            if count == frequency - 1:
                highFreq = price
        frequency = max(frequency, count)
    print("Frequency: " + str(frequency))
    print("LowFreq: " + str(lowFreq))
    print("HighFreq: " + str(highFreq) + "\n")
    return lowFreq*1.05, highFreq*1.05
