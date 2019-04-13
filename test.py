import stock.analyze_stocks as analyze_stocks
import stock.run as run
from datetime import date, timedelta

print(("sudo Rscript plot.R " + (date.today()-timedelta(days = 30)).strftime("%Y-%m-%d") + " " + date.today().strftime("%Y-%m-%d") + " " + "AAPL"))
