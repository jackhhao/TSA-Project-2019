import requests
import lxml.html
import sys
import nltk
import time

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from urllib.request import urlopen
from bs4 import BeautifulSoup

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

urlList = []

i = input("symbol: ")

page = urlopen('https://finance.yahoo.com/quote/' + str(i) + "/press-releases?p=" + str(i)).read()
soup = BeautifulSoup(page, features="html.parser")
posts = soup.findAll("h3", {"class": "Mb(5px)"})
x = 0
for post in posts:
    x+=1
    time.sleep(1)
    url = post.a['href']
    url = modify(url)
    urlList.append(url)
    if(x==10):
        break

def urls():
    return urlList
