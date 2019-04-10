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

@app.route('/convert/')
def translate():
    translated = request.args.get('v')
    return stock.run.final(translated)

@app.route('/random/')
def random():
    return stock.run.randomStock()

@app.route('/price')
def getPrice():
    translated = request.args.get('v')
    return stock.run.getPrice(rc)
@app.route('/suggest/')
def suggest():
    rc = request.args.get('v')
    return stock.run.suggest(rc)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
