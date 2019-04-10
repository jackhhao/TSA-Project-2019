import os
import stock.run
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/s/')
def returnG():
    return app.send_static_file('generic.html')

@app.route('/c/')
def returnC():
    return app.send_static_file('elements.html')

@app.route('/suggest/')
def suggest():
    suggested = request.args.get('v')
    return stock.run.main(suggested)

@app.route('/convert/')
def translate():
    translated = request.args.get('v')
    return stock.run.final(translated)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

if __name__ == '__main__':
    #stock.run.main(20)
    app.run(debug=True, port=5050)
