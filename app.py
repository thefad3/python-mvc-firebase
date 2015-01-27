import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import hashlib
from firebase import firebase
firebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/', None)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signupAction', methods=['GET', 'POST'])
def addUser():
    password = request.form['password']
    username = request.form['username']
    sha1 = hashlib.sha1()
    sha1.update(password)
    password = sha1.hexdigest()
    #Database Directive
    firebase.post('/users/', 
    #Create Sub categories
    #Careful, looks like javascript xD
    {
    'usern': username,
    'userp': password    
    }
    )
    return 'It worked :D congrats' 


@app.route('/signup')
def regForm():
    return render_template('adduser.html')
    

    
        
    



#The Line below is REQUIRED to run on C9    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
if __name__ == '__main__':
    app.run()