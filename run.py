import os
import analyzeData
import multiprocessing

from csv import reader
from random import choice
from time import sleep

f= open("companyList.csv")
r = reader(f, delimiter=",")
tl = [i[0] for i in r]

tl = ["AAPL", "GOOG", "FB", "QCOM", "AMD"]
if __name__ == '__main__':
    amt = int(input("How many stocks would you like to go through? "))
    p = multiprocessing.Pool(amt)
    ls = [choice(tl) for _ in range(0, amt)]
    print(ls)
    p.map(analyzeData.AD, ls)
