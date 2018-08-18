from keys import *
import requests, json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect, session, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_oauthlib.client import OAuth
from requests_oauthlib import OAuth2Session
from flask.json import jsonify
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

#POST and GET request to OAuth endpoint fails
"""
res = requests.request("POST", req_url, headers = params)
print('Post request to req_ulr')
print(res.text)

res = requests.request("GET", req_url, headers = params)
print('GET request to req_ulr')
print(res.text)
"""

print('Get request sent to urlcheck receives info on Sneak Em Account')
response = requests.request("GET", urlcheck, headers=headers_one)
print(response.text)

#Authorization through user-agent, currently sends out right, not sure about response
"""
oauth = OAuth2Session(cid, redirect_uri = callback, scope = 'check')
authorization_url, state = oauth.authorization_url(req_url)
redirect(authorization_url)
print()

response_oauth = requests.request("GET", authorization_url, headers = params)
print ('Authorization_url: %s' % authorization_url)
print('response_oauth is given as: %s' % response_oauth)
print(response_oauth.text)
# auth_resp = input(callback)
# print(auth_resp)
"""

# Supposedly included only for development side, once launched can remove this as it should be https
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


#attempt two
class testForm(FlaskForm):
    submit = SubmitField("Connect to CB")

@app.route('/authorize')
def authorize():
    cbook = OAuth2Session(cid, scope = 'check')
    authorization_url, state = cbook.authorization_url(req_url)
    print(f'go to %s and authorize' % authorization_url)
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback', methods = ["GET"])
def callback():
    print('Entered callback and has been redirected to /callback on client side')
    print('Entered callback and has been redirected to /callback on client side')
    print('Entered callback and has been redirected to /callback on client side')
    cbook = OAuth2Session(cid, redirect_uri = callback, state = session['oauth_state'])
    print('Initializing cbook OAuth2Session seems to work okay')
    token = cbook.fetch_token(urlToken, client_secret = (apikey + ':' + apisecret), authorization_response = request.url)
    session['oauth_token'] = token
    flash('Successfully got token I think! lol...', 'success')
    return redirect(url_for('home'))

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = testForm()
    if form.validate_on_submit():
        print('validate_on_submit entered')
        flash('Submitted', 'success')
        return redirect(url_for('authorize'));
    return render_template('layout.html', title = 'Test', form = form)

"""
response = requests.request("GET", 'https://checkbook.io/oauth/authorize', headers = params)
print('Attempt using requests results in:')
print(response)
"""

if __name__ == '__main__':
    app.run(debug=True)
