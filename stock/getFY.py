import requests
import lxml.html
import sys

from urllib.request import urlopen
from bs4 import BeautifulSoup

urlType = ""
headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

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
        url = post.a['href']
        url = modify(url)
        urlList.append(url)
        if(x==10):
            break
    return urlList

def convos(ticker):
    r = requests.get("https://finance.yahoo.com/quote/"+ticker+"/community?p="+ticker, headers = headers)
    soup = BeautifulSoup(r.content, features="html.parser")
    convos = soup.findAll("div", {"class": "C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)"})
    return  [convo.text for convo in convos]
