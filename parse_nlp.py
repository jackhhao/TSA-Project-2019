from __future__ import (absolute_import, division, print_function,
                            unicode_literals)
import requests
import lxml.html

import backtrader as bt
import backtrader.indicators as btind
import os.path
import sys
import nltk
import warnings
warnings.filterwarnings('ignore')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import pprint

html = requests.get('https://abcnews.go.com/Business/story?id=3457209&page=1')
doc = lxml.html.fromstring(html.content)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

passage = """
"""
i = input("symbol: ")

page = urlopen('https://finance.yahoo.com/quote/' + str(i) + "?p=" + str(i)).read()
soup = BeautifulSoup(page, features="html.parser")
posts = soup.findAll("h3", {"class": "Mb(5px)"})
for post in posts:
    print(post)
    time.sleep(1)
    url = post.a['href']
    #date = post.time.text
    #print(date, url)
    if url[0] == "/":
        url = "https://finance.yahoo.com" + url
    print(url)
    if ("/video/" not in url):
        try:
            link_page = urlopen(url).read()
        except:
            url = url[:-2]
            link_page = urlopen(url).read()
        link_soup = BeautifulSoup(link_page)
        sentences = link_soup.findAll("p")
        passage = ""
        for sentence in sentences:
            print(sentence)
            passage += sentence.text
        sentiment = sia.polarity_scores(passage)['compound']
        print("Sentiment Score:", sia.polarity_scores(passage)['compound'])
        #date_sentiments.setdefault(date, []).append(sentiment)

