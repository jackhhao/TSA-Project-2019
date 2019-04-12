import os
import stock.run
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def hRoot():
    return app.send_static_file('index.html')

@app.route('/portfolio/')
def pRoot():
    return app.send_static_file("portfolio.html")

@app.route('/stocks/')
def sRoot():
    return app.send_static_file("stocks.html")

@app.route('/lookup/')
def lookup():
    fetched = request.args.get('v')
    return stock.run.final(fetched)

@app.route('/random/')
def random():
    return stock.run.randomStock()

@app.route('/volume/')
def volume():
    rc = request.args.get('v')
    return str(stock.run.returnVolume(rc))

@app.route('/volatility/')
def volatility():
    fetched = request.args.get('v')
    return str(stock.run.returnVolatility(fetched))

@app.route('/beta/')
def beta():
    fetched = request.args.get('v')
    return str(stock.run.returnBeta(fetched)) 

@app.route('/price/')
def price():
    rc = request.args.get('v')
    return str(stock.run.getPrice(rc))

@app.route('/suggest/')
def qSuggest():
    rc = request.args.get('v')
    return str(stock.run.quickSuggest(rc))

@app.route('/suggest_full/')
def fSuggest():
    rc = request.args.get('v')
    return str(stock.run.fullSuggest(rc))


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
