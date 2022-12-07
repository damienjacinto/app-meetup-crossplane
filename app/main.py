import os
from flask import Flask
from flask import render_template
import json

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static')

f = open('./app/data.json')
data = json.load(f)

@app.route("/")
def hello_world():
    return render_template('index.html', messages=data['messages'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)