import os
from flask import Flask
from flask import render_template
from flask_modals import Modal
import json

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static')
modal = Modal()
modal.init_app(app)

f = open('./data.json')
data = json.load(f)

@app.route("/")
def hello_world():
    return render_template('index.html', messages=data['messages'])

if __name == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)