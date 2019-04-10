import os
import multiprocessing
import stock.analyze_stocks as analyze_stocks
import webbrowser
import pip
import subprocess as s

from time import sleep
from csv import reader
from random import choice
from time import sleep
from math import exp
#from win10toast import ToastNotifier

#toaster = ToastNotifier()
count = 0
usedStocks = []

def AD(rc):
    vl = analyze_stocks.getVolume(rc)
    senA = analyze_stocks.sentimentArticles(rc)
    senC = analyze_stocks.sentimentConvos(rc)
    vt = analyze_stocks.getVolatility(rc, 5)
    h = analyze_stocks.getHL(rc, 5, "High")
    l = analyze_stocks.getHL(rc, 5, "Low")
    print ("Stock: {} \n\tVolume: {} \n\tVolatility: {} \n\tSentiment and Magnitude of Articles: {} \n\tSentiment and Magnitude of Conversations: {}\n\tHigh: {high}\n\tLow: {low} \n\tRating: {rating}".format(rc, vl, vt, senA, senC, high = h, low = l, rating = suggest(rc)))
    multiprocessing.Process(target=nu, args=(rc, h, l, )).start()

def nu(rc, h, l):
    while(True):
        if(h is not None or l is not None):
            if(analyze_stocks.getCurrentPrice(rc) == l):
                s.call(["notify-send", "-i", "../assets/money.jpeg", "Buy stock {stock} right now!".format(stock = rc)])
                #toaster.show_toast("Stock Bot", "Buy stock {stock} right now!".format(stock = rc), duration = 10)
                print("Enter a stock to lookup: ")
                break
            elif(analyze_stocks.getCurrentPrice(rc) == h):
                s.check_call(["notify-send", "-i", "../assets/money.jpeg", "Sell stock {stock} right now!".format(stock = rc)])
                #toaster.show_toast("Stock Bot", "Sell stock {stock} right now! Go to console.".format(stock = rc), duration = 10)
                print("Enter a stock to lookup: ")
                break
        else:
            break

def final(rc):
    sellAt = analyze_stocks.getHL(rc, 10, "High")
    buyAt = analyze_stocks.getHL(rc, 10, "Low")

    try:
        buyAt = '${0:.2f}'.format(buyAt)
        sellAt = '${0:.2f}'.format(sellAt)
    except TypeError:
        pass

    return "We recommend that you buy at {x} and sell at {y}.".format(x = buyAt, y = sellAt)

f= open("assets/companyList.csv")
r = reader(f, delimiter=",")
tl = [i[0] for i in r]

def suggest(rc):
    rating = 0
    vl = analyze_stocks.getVolume(rc)
    if (vl is None):
        return 0
    #print("The stock (" + rc + ") is operating at a volume of " + str(vl) + " shares on the last open trading day.")
    vlRating = 100/(1 + 24.5*(exp(-vl/1000000)))
    #print("The StockBot gives the stock a volume rating of " + str(vlRating) + ".")
    senA = analyze_stocks.sentimentArticles(rc)[0]
    senC = analyze_stocks.sentimentConvos(rc)[0]
    vt = analyze_stocks.getVolatility(rc, 10)
    ac = analyze_stocks.getActualVolatility(rc, 10)
    try:
        sentiment = ((senA*100)+(senC*100))/2
    except:
        sentiment = 0
        rating -= 1000
    rating = sentiment + vt*60 - abs(ac*40) + vlRating
    return rating

def randomStock():
    rc = 0
    while rc in usedStocks:
        rc = choice(tl)
    usedStocks.append(rc)
    
def AD(rc):
    vl = analyze_stocks.getVolume(rc)
    senA = analyze_stocks.sentimentArticles(rc)
    senC = analyze_stocks.sentimentConvos(rc)
    vt = analyze_stocks.getVolatility(rc, 10)
    ac = analyze_stocks.getActualVolatility(rc, 10)
    h = analyze_stocks.getHL(rc, 10, "High")
    l = analyze_stocks.getHL(rc, 10, "Low")
    print ("Stock: {} \n\tVolume: {} \n\tVolatility: {} \n\tActual Volatility: {} \n\tSentiment and Magnitude of Articles: {} \n\tSentiment and Magnitude of Conversations: {}\n\tHigh: {high}\n\tLow: {low} \n\tRating: {rating}".format(rc, vl, vt, ac, senA, senC, high = h, low = l, rating = suggest(rc)))
    multiprocessing.Process(target=nu, args=(rc, h, l, )).start()

def main(amt):
    ls = []
    x = lambda a : a if a not in ls else x(choice(tl))
    ls = [x(choice(tl)) for _ in range(0, amt)]
    print(ls)
    pl = [multiprocessing.Process(target=AD, args=(i,)) for i in ls]
    for i in pl:
        i.start()
    sleep(20)
    while(True):
        ticker = input()
        if(analyze_stocks.getCurrentPrice(ticker) is not None):
            print("Opening {stock}!".format(stock = ticker))
            webbrowser.open('https://finance.yahoo.com/quote/{ticker}?p={ticker}'.format(ticker = ticker))
        elif(ticker == "quit"):
            break
