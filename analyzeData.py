import analyze_stocks
import csv
import os

from random import choice

def AD(rc):
    vl = str(analyze_stocks.getVolume(rc))
    senA = analyze_stocks.sentimentArtciles(rc)
    vt = str(analyze_stocks.getVolatility(rc, 5))
    print ("Stock: {} \n\tVolume: {} \n\tVolatility: {} \n\tSentiment and Magnitude of Articles: {} \n\tSentiment and Magnitude".format(rc, vl, vt, senA))
