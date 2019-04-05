import analyze_stocks
import csv
from random import choice

with open("companyList.csv") as f:
    r = csv.reader(f, delimiter=",")
    tl = [i[0] for i in r]

rc = choice(tl)
print(rc)
rc = "AAPL"
vl = analyze_stocks.getVolume(rc)
print(vl)
analyze_stocks.sentiment(rc)
vt = analyze_stocks.getVolatility(rc, 5)
print(vt)
if((vl+vt)/3 > 0.5):
    print("Buy stock ", rc, " at: ", analyze_stocks.getHL(rc, 5, "Low"), "\nand sell at: ", analyze_stocks.getHL(rc, 5, "High"))
print("End")
