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
app = Flask(__name__)
app.secret_key = "baconMang"
firebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/', None)

@app.route('/signupAction', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        #Generates Random UID for Database
        idx = uuid.uuid4()
        uid = str(idx)
        password = request.form['password']
        username = request.form['username']
        #Hash that Passsword
        sha1 = hashlib.sha1()
        sha1.update(password)
        password = sha1.hexdigest()
        #Database Directive
        firebase.put('/users', username,
        {
        'uid': uid,
        'usern': username,
        'userp': password  
        }
        )
        return redirect('/login')
    else:
        return redirect('/signup')

@app.route('/addAction', methods=['GET', 'POST'])
def addSecondary():
    if request.method == 'POST':
        #Checking for session before allowing on Login Section
        if session['session']:
            #Generates Random UID for Database
            idx = uuid.uuid4()
            uid = str(idx)
            password = request.form['password']
            username = request.form['username']
            #Hash that Passsword
            sha1 = hashlib.sha1()
            sha1.update(password)
            password = sha1.hexdigest()
            #Database Directive
            firebase.put('/users', username,
            {
            'uid': uid,
            'usern': username,
            'userp': password  
            }
            )
            return redirect('/protected')
        else:
            return redirect('/protected')


@app.route('/loginAction', methods=['GET', 'POST'])
def loginAction():
    if request.method == 'POST':
        username = request.form['username']
        uVer = firebase.get('/users', username)
        password = request.form['password']
        sha1 = hashlib.sha1()
        sha1.update(password)
        password = sha1.hexdigest()
        if uVer['userp'] == password:
            session['session'] = username
            return redirect('/protected')
    else:
        return redirect('/login')
        
@app.route('/updateForm/<id>')
def updateForm(id):
    if session['session']:
        data = firebase.get('/users', id)
    else: 
        return redirect('/login')
    return render_template('updateform.html', data=data)

@app.route('/updateAction/<id>', methods=['GET', 'POST'])
def updateAction(id):
    username = request.form['username']
    password = request.form['password']
    sha1 = hashlib.sha1()
    sha1.update(password)
    password = sha1.hexdigest()
    idx = uuid.uuid4()
    uid = str(idx)
    firebase.put('/users', username,
    {
            'uid': uid,
            'usern': username,
            'userp': password  
    }
    )
    return redirect('/protected')
  
#Page Renderings below
#Trying to seperate the logic of the system from the display 
#Most page route will return just a render template or the HTML
@app.route('/signup')
def regForm():
    return render_template('adduser.html')

@app.route('/protected')
def protect():
    if session['session']:
        data = firebase.get('/users', None)
        return render_template('protected.html', data=data)
    else:
        return redirect('/login')

@app.route('/delete/<id>')
def delete(id):
    if session['session']:
        firebase.delete('/users', id)
        return redirect("/protected")
    else: 
        return redirect('/login')
        
@app.route('/adduser')
def addPage():
    if session['session']:
        return render_template('add.html')
    else:
        return redirect('/protected')

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('session', None)
    return redirect('/login')
    
@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(500)
def serverError(error):
    return render_template('500.html'), 500

#The Line below is REQUIRED to run on C9    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
if __name__ == '__main__':
    app.run()
    app.debug(True)