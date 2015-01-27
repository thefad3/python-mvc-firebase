from flask import Flask
import hashlib
import os
from flask import session
import mysql.connector
from flask import request
from flask import render_template
from flask import redirect, url_for, send_from_directory
from werkzeug import secure_filename
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "1234"

@app.route('/protected')
def protected():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', port='8889', database='ssl')
    cursor = cnx.cursor()
    cursor.execute("select * from users")
    users = cursor.fetchall()
    return render_template('protected.html', data=users)

@app.route('/loginform')
def loginForm():
    return render_template('loginform.html')

@app.route('/')
def index():
    return redirect('/loginform')

@app.route('/addAction', methods=['GET', 'POST'])
def addForm():
    if request.method == 'POST':
        cnx = mysql.connector.connect(user='root', password='root', host='localhost', port='8889', database='ssl')
        cursor = cnx.cursor()
        password = request.form['password']
        sha1 = hashlib.sha1()
        sha1.update(password)
        password = sha1.hexdigest()
        cursor.execute("insert into users (username, password) values(%s,%s)", (request.form['username'], password))
        cnx.commit()
        return redirect('/protected')
    else:
        return request.method

@app.route('/addForm')
def viewForm():
    return render_template('addform.html')

@app.route('/updateForm/<id>')
def updateForm(id):
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', port='8889', database='ssl')
    cursor = cnx.cursor()
    idx = (id,)
    sql = "select * from users where id=%s"
    cursor.execute(sql, idx)
    user = cursor.fetchone()
    return render_template('updateform.html', data=user)

@app.route('/updateAction/<id>', methods=['GET', 'POST'])
def updateAction(id):
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', port='8889', database='ssl')
    cursor = cnx.cursor()
    username = request.form['username']
    password = request.form['password']
    sha1 = hashlib.sha1()
    sha1.update(password)
    password = sha1.hexdigest()
    cursor.execute("update users set username=%s, password=%s where id=%s", (username, password, id))
    cnx.commit()
    return redirect('/protected')

@app.route('/delete/<id>')
def delete(id):
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', port='8889', database='ssl')
    cursor = cnx.cursor()
    idx = (id,)
    cursor.execute("delete from users where id=%s", (idx))
    cnx.commit()
    return redirect("/protected")

@app.route('/logout')
def logout():
    session.pop('logged', None)
    return redirect("/loginform")


@app.route('/loginAction', methods=['GET', 'POST'])
def loginAction():
    if request.method == 'POST':
        cnx = mysql.connector.connect(user='root', password='root', host='localhost', port='8889', database='ssl')
        cursor = cnx.cursor()
        username = request.form['username']
        password = request.form['password']
        hashed = hashlib.sha1()
        hashed.update(request.form['password'])
        cursor.execute("select * from users where username=%s and password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            stuff = {
                'username': username,
                'password': password
            }
            session["logged"] = 1
            return redirect("/protected")
        else:
            session["logged"] = 0
            return redirect("/loginform")

        cnx.close()
    else:
        return request.method


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)