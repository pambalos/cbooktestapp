from keys import *
import requests, json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_oauthlib.client import Oauth

app = Flask(__name__)
app.config['SECRET_KEY'] =' 67aGHYDS8c7S8CGcaydw878csa7887bac' #setting secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

params = {
    'client_id': cid,
    'response_type': 'code',
    'scope': 'check',
    'redirect_uri': callback
}

client = BackendApplicationClient(client_id = cid)
oauth = requests.Session(client_id = client)
token = oauth.fetch_token(token_url = urlToken, client_id = cid, client_secret = apisecret)

response = requests.request("GET", 'https://checkbook.io/oauth/authorize', headers = params)
print('Attempt using requests results in:')
print(response)

#attempt two
heads_test = {"Content-Type" : "application/json", "X-Accept" : "application/json"}
payload = {"client_id" : cid, "redirect_uri" : callback}

class testForm(FlaskForm):
    submit = SubmitField("Connect to CB")

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = testForm()
    if form.validate_on_submit():
        flash('Submitted', 'success')
        return redirect();
    return render_template('layout.html', title = 'Test', form = form)

if __name__ == '__main__':
    app.run(debug=True)
