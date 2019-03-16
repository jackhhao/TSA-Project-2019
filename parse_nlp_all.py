from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests
import lxml.html

#import backtrader as bt
#import backtrader.indicators as btind
import os.path
import sys
import nltk
import warnings
warnings.filterwarnings('ignore')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from urllib.request import urlopen
from bs4 import BeautifulSoup
#from datetime import datetime, timedelta
import time
import pprint

html = requests.get('https://abcnews.go.com/Business/story?id=3457209&page=1')
doc = lxml.html.fromstring(html.content)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

def modify(url):
    if url[0] == "/":
        url = "https://finance.yahoo.com" + url
    if "https://finance.yahoo.com/m" in url:
        page = urlopen(url).read()
        soup = BeautifulSoup(page, features="html.parser")
        read_more = soup.find("div", {"class": "read-more Mt(20px) Ta(start) Ta(c)--sm"})
        url = read_more.a['href']
    return url

def getSentiment(passage):
    sentiment = sia.polarity_scores(passage)['compound']
    return ("Sentiment Score:" + str(sia.polarity_scores(passage)['compound']))

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

    url = modify(url)
    print(url)
    if ("/video/" not in url):
        r = requests.get(url, headers=headers)
        link_soup = BeautifulSoup(r.content)
        sentences = link_soup.findAll("p")
        passage = ""

        for sentence in sentences:
            print(sentence.text)
            passage += sentence.text
        print(getSentiment(passage))
            #date_sentiments.setdefault(date, []).append(sentiment)