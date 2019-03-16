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
#import nlp_summary

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

#cont = "yes"

def getSentiment(passage):
    sentiment = sia.polarity_scores(passage)['compound']
    return ("\nSentiment Score:" + str(sia.polarity_scores(passage)['compound']))

#while (cont != "no"):
def main(url):
    page = urlopen(str(url)).read()

    link_soup = BeautifulSoup(page)

    sentences = link_soup.findAll("p")

    passage = ""

    for sentence in sentences:
        print(sentence.text)
        passage += sentence.text
    print(getSentiment(passage))
    return passage

    #nlp_summary.generate_summary( passage, len(passage)/3.0)
    #date_sentiments.setdefault(date, []).append(sentiment)
    #cont = input("\ncont? ")