import requests
import lxml.html
import sys
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup

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

def urls(ticker):
    urlList = []

    page = urlopen('https://finance.yahoo.com/quote/' + ticker + "/press-releases?p=" + ticker).read()
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
    return urlList
