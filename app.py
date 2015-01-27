import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
import json
import uuid 
import hashlib
from firebase import firebase
firebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/users/', None)
app = Flask(__name__)

@app.route('/signupAction', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        idx = uuid.uuid4()
        uid = str(idx)
        password = request.form['password']
        username = request.form['username']
        #Hash that Passsword
        sha1 = hashlib.sha1()
        sha1.update(password)
        password = sha1.hexdigest()
        #Database Directive
        firebase.post(uid,
        {
        'uid': uid,
        'usern': username,
        'userp': password  
        }
        )
        return redirect('/protected')
    else:
        return redirect('/signup')


    
@app.route('/loginAction', methods=['GET', 'POST'])
def loginAction():
    if request.method == 'POST':
        return 'dkjhfk'
    else:
        return redirect('/signup')
        
#Page Renderings below
#Trying to seperate the logic of the system from the display 
#Most page route will return just a render template or the HTML

@app.route('/signup')
def regForm():
    return render_template('adduser.html')

@app.route('/protected')
def protect():
    udi = 'f0d549c6-eef1-4ca5-8024-7bd2db5bbd34'
    #Calls the location by the defined var
    #Need to pass int he ID Some how...
    userInfo = firebase.get(udi, None)
    return render_template('protected.html', data=userInfo)

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