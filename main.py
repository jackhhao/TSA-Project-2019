import os
import stock.run
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/convert/')
def translate():
    translated = request.args.get('v')
    return stock.run.final(translated)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< Updated upstream
    stock.run.main(20)
=======
    stock.run.main(10)
>>>>>>> Stashed changes
=======
>>>>>>> 70f0dce9d204ba839bfbbbb28db6490eb93a768c
    app.run(debug=True, port=5050)
    stock.run.main(10)
