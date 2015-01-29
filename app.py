import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session, redirect, url_for, escape
from flask import redirect
import json
import uuid 
import hashlib
from firebase import firebase
from pprint import pprint
from firebase_token_generator import create_token
firebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/', None)
app = Flask(__name__)
app.secret_key = "baconMang"

@app.route('/signupAction', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        idx = uuid.uuid4()
        uid = str(idx)
        password = request.form['password']
        username = request.form['username']
        dbUrl = '/users/' + username
        #Hash that Passsword
        sha1 = hashlib.sha1()
        sha1.update(password)
        password = sha1.hexdigest()
        #Database Directive
        firebase.put(dbUrl, uid,
        {
        'uid': uid,
        'usern': username,
        'userp': password  
        }
        )
        #session['logged']
        return redirect('/login')
    else:
        return redirect('/signup')


@app.route('/loginAction', methods=['GET', 'POST'])
def loginAction():
    authentication = firebase.FirebaseAuthentication('x2uoh7WO7nzWKhgijadq18IPGbOTKRFxHJ4pX1JA', 'chrisl')
    firebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/', authentication)
    print authentication


        
#Page Renderings below
#Trying to seperate the logic of the system from the display 
#Most page route will return just a render template or the HTML

@app.route('/signup')
def regForm():
    return render_template('adduser.html')

@app.route('/protected')
def protect():
    #udi = session['logged']
    #Calls the location by the defined var
    #Need to pass int he ID Some how...
    udi = '/users/chrisl'
    userInfo = firebase.get(udi, None)
    jsonData = json.loads(userInfo)
    return render_template('protected.html', data=jsonData)

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')


#The Line below is REQUIRED to run on C9    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
if __name__ == '__main__':
    app.run()
    app.debug(True)