from keys import *
import requests, json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] =' 67aGHYDS8c7S8CGcaydw878csa7887bac' #setting secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

params = {'client_id': cid, 'response_type': 'code', 'scope': 'check', 'redirect_uri': callback}

response = requests.request("POST", 'https://checkbook.io/oauth/authorize'
, headers = params)
print('Attempt using requests results in:')
print(response)

#attempt two
heads_test = {"Content-Type" : "application/json", "X-Accept" : "application/json"}
payload = {"client_id" : cid, "redirect_uri" : callback}

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html', title = 'Test')

if __name__ == '__main__':
    app.run(debug=True)
