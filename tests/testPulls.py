from keys import *
import requests, json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect, session, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_oauthlib.client import OAuth
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
app.config['SECRET_KEY'] ='sZWjFJmyFQnzkVMxbFCTbByZNJhaJV' #setting secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

params = {
    'client_id': cid,
    'response_type': 'code',
    'scope': 'check',
    'redirect_uri': callback
}

paramstwo = {
    'client_id' : cid,
    'grant_type' : authc,
}

urlcheck = "https://sandbox.checkbook.io/v3/check"
headers_one = {
  'Accept': 'application/json',
  'Authorization': (apikey + ':' + apisecret)
}

headers_two = {
  'Content-Type': 'application/json',
  'Authorization': (apikey + ':' + apisecret)
}

response = requests.request("GET", urlcheck, headers=headers_one)
print(response.text)
'''
#Authorization through user-agent, currently sends out right, not sure about response
oauth = OAuth2Session(cid, redirect_uri = callback, scope = 'check')
authorization_url, state = oauth.authorization_url(req_url)
response_oauth = requests.request("GET", authorization_url, headers = params)
print ('Authorization_url: %s' % authorization_url)
print('response_oauth is given as: %s' % response_oauth)
print(response_oauth.text)
# auth_resp = input(callback)
# print(auth_resp)
'''


#attempt two
class testForm(FlaskForm):
    submit = SubmitField("Connect to CB")

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = testForm()
    if form.validate_on_submit():
        print('validate_on_submit entered')
        flash('Submitted', 'success')
        return redirect(authorization_url, code = 302);
    return render_template('layout.html', title = 'Test', form = form)

"""
response = requests.request("GET", 'https://checkbook.io/oauth/authorize', headers = params)
print('Attempt using requests results in:')
print(response)
"""

if __name__ == '__main__':
    app.run(debug=True)
