import os
from flask import Flask, request, render_template
import json
from date_calendar import DateCalender
from database import db
from utils import greyOutDate

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static')

database_enable = bool(os.environ.get('DATABASE_ENABLE', ""))

if database_enable:
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///test.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    db.init_app(app)
    with app.app_context():
        db.create_all()

path_data = os.environ.get('DATA_PATH', './app/data.json')
f = open(path_data)
data = json.load(f)


@app.route("/")
def index():
    title = "Calendrier de l'avent 2022"
    messages = data['messages']
    if database_enable:
        res = db.session.query(DateCalender).all()
        messages = greyOutDate(res, messages)
    return render_template('index.html', messages=messages, title=title)


@app.route('/update', methods=['POST'])
def update():
    if database_enable:
        date = request.form['date']
        dc = DateCalender(date=date)
        db.session.add(dc)
        db.session.commit()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
