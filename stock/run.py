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
#from win10toast import ToastNotifier

#toaster = ToastNotifier()
count = 0

def AD(rc):
    vl = analyze_stocks.getVolume(rc)
    senA = analyze_stocks.sentimentArticles(rc)
    senC = analyze_stocks.sentimentConvos(rc)
    vt = analyze_stocks.getVolatility(rc, 5)
    h = analyze_stocks.getHL(rc, 5, "High")
    l = analyze_stocks.getHL(rc, 5, "Low")
    print ("Stock: {} \n\tVolume: {} \n\tVolatility: {} \n\tSentiment and Magnitude of Articles: {} \n\tSentiment and Magnitude of Conversations: {}".format(rc, vl, vt, senA, senC))
    multiprocessing.Process(target=nu, args=(rc, h, l, )).start()

def nu(rc, h, l):
    while(True):
        if(h is not None or l is not None):
            if(analyze_stocks.getCurrentPrice(rc) == l):
                s.check_call(["notify-send", "-i", "/home/usr/Downloads/money.jpeg", "Buy stock {} stock right now!".format(stock = rc)])
                #toaster.show_toast("Stock Bot", "Buy stock {stock} right now!".format(stock = rc), duration = 10)
                print("Enter a stock to lookup: ")
                break
            elif(analyze_stocks.getCurrentPrice(rc) == h):
                s.check_call(["notify-send", "-i", "/home/usr/Downloads/money.jpeg", "Sell stock {} stock right now!".format(stock = rc)])
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

def main(amt):
    ls = []
    x = lambda a : a if a not in ls else x(choice(tl))
    ls = [x(choice(tl)) for _ in range(0, amt)]
    print(ls)
    pl = [multiprocessing.Process(target=AD, args=(i,)) for i in ls]
    for i in pl:
        i.start()
    sleep(100)
    while(True):
        ticker = input()
        if(analyze_stocks.getCurrentPrice(ticker) is not None):
            print("Opening {stock}!".format(stock = ticker))
            webbrowser.open('https://finance.yahoo.com/quote/{ticker}?p={ticker}'.format(ticker = ticker))
        elif(ticker == "quit"):
            break
