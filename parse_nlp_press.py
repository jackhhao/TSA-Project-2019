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
urlType = ""

def modify(url):
    if url[0] == "/":
        url = "https://finance.yahoo.com" + url
    if "https://finance.yahoo.com/m" in url:
        page = urlopen(url).read()
        soup = BeautifulSoup(page, features="html.parser")
        read_more = soup.find("div", {"class": "read-more Mt(20px) Ta(start) Ta(c)--sm"})
        url = read_more.a['href']
        urlType = "non"
    return url
"""
def getPage(url):
    if (urlType == "non"):
        link_page = requests.get(url, headers=headers)
    else:
        link_page = urlopen(url).read()
    return link_page
"""
def getSentiment(passage):
    sentiment = sia.polarity_scores(passage)['compound']
    return ("                                        Sentiment Score:" + str(sia.polarity_scores(passage)['compound']))

i = input("symbol: ")

#https://finance.yahoo.com/quote/CSCO/press-releases?p=CSCO

page = urlopen('https://finance.yahoo.com/quote/' + str(i) + "/press-releases?p=" + str(i)).read()
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
        if urlType == "non":
            r = requests.get(url, headers=headers)
            link_page = r.content
            print("urlType is non")
        else:
            link_page = urlopen(url).read()
        link_soup = BeautifulSoup(link_page)
        sentences = link_soup.findAll("p")

        passage = ""

        for sentence in sentences:
            if "Fz(14px) Lh(19px) Fz(13px)--sm1024 Lh(17px)--sm1024 LineClamp(2,38px) LineClamp(2,34px)--sm1024 M(0)" in sentence["class"]:
                continue
            else:
                print(sentence.text)
                passage += sentence.text
        print(getSentiment(passage))
            #date_sentiments.setdefault(date, []).append(sentiment)