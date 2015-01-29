{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask\nfrom flask import render_template\nfrom flask import request\nfrom flask import session, redirect, url_for, escape\nfrom flask import redirect\nimport json\nimport uuid \nimport hashlib\nfrom firebase import firebase\nfrom pprint import pprint\nfrom firebase_token_generator import create_token\napp = Flask(__name__)\napp.secret_key = \"baconMang\"\nfbAuthSecretKey = 'x2uoh7WO7nzWKhgijadq18IPGbOTKRFxHJ4pX1JA'\n#auth = firebase.FirebaseAuthentication(fbAuthSecretKey, 'thefad3@gmail.com', 'fsdf')\nfirebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/')\n\n@app.route('/signupAction', methods=['GET', 'POST'])\ndef addUser():\n    if request.method == 'POST':\n        idx = uuid.uuid4()\n        uid = str(idx)\n        password = request.form['password']\n        username = request.form['username']\n        #Hash that Passsword\n        sha1 = hashlib.sha1()\n        sha1.update(password)\n        password = sha1.hexdigest()\n        #Database Directive\n        firebase.put('/users', username,\n        {\n        'uid': uid,\n        'usern': username,\n        'userp': password  \n        }\n        )\n        return redirect('/login')\n    else:\n        return redirect('/signup')\n\n\n@app.route('/loginAction')\ndef loginAction():\n    password = request.form['password']\n    username = request.form['username']\n    sha1 = hashlib.sha1()\n    sha1.update(password)\n    password = sha1.hexdigest()\n    auth = firebase.FirebaseAuthentication(fbAuthSecretKey, username, password)\n    firebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/', auth)\n    \n    #Using protected vars were able to return tokens based on what we want to get\n    #Prints or \"returns\" long string of information but can be decoded with json decoder\n    #Next to conform data\n    firebase.auth = auth\n    user = auth.get_user()\n    return user.firebase_auth_token\n\n  \n#Page Renderings below\n#Trying to seperate the logic of the system from the display \n#Most page route will return just a render template or the HTML\n\n@app.route('/signup')\ndef regForm():\n    return render_template('adduser.html')\n\n@app.route('/protected')\ndef protect():\n    #udi = session['logged']\n    #Calls the location by the defined var\n    #Need to pass int he ID Some how...\n    udi = '/users/chrisl'\n    userInfo = firebase.get(udi, None)\n    jsonData = json.loads(userInfo)\n    return render_template('protected.html', data=jsonData)\n\n@app.route('/login')\ndef loginPage():\n    return render_template('login.html')\n\n@app.route('/')\ndef index():\n    return render_template('index.html')\n\n\n#The Line below is REQUIRED to run on C9    \napp.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))\nif __name__ == '__main__':\n    app.run()\n    app.debug(True)","undoManager":{"mark":51,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":45,"column":79},"end":{"row":45,"column":80},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":80},"end":{"row":45,"column":81},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":81},"end":{"row":45,"column":82},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":81},"end":{"row":45,"column":82},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":81},"end":{"row":45,"column":82},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":82},"end":{"row":45,"column":83},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":83},"end":{"row":45,"column":84},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":84},"end":{"row":45,"column":85},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":85},"end":{"row":45,"column":86},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":86},"end":{"row":45,"column":87},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":87},"end":{"row":45,"column":88},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":88},"end":{"row":46,"column":0},"action":"insert","lines":["",""]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":4},"end":{"row":46,"column":5},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"insert","lines":["N"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":7},"end":{"row":46,"column":8},"action":"insert","lines":["x"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":8},"end":{"row":46,"column":9},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":13},"end":{"row":46,"column":14},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":15},"end":{"row":46,"column":16},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":16},"end":{"row":46,"column":17},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":17},"end":{"row":46,"column":18},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":20},"end":{"row":46,"column":21},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":21},"end":{"row":46,"column":22},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":22},"end":{"row":46,"column":23},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":24},"end":{"row":46,"column":25},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":78},"end":{"row":15,"column":84},"action":"remove","lines":["usr123"]},{"start":{"row":15,"column":78},"end":{"row":15,"column":79},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":79},"end":{"row":15,"column":80},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":80},"end":{"row":15,"column":81},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":81},"end":{"row":15,"column":82},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":79},"end":{"row":16,"column":80},"action":"remove","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":78},"end":{"row":16,"column":79},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":77},"end":{"row":16,"column":78},"action":"remove","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":76},"end":{"row":16,"column":77},"action":"remove","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":75},"end":{"row":16,"column":76},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":74},"end":{"row":16,"column":75},"action":"remove","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":43,"column":18},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":4},"end":{"row":45,"column":81},"action":"insert","lines":["auth = firebase.FirebaseAuthentication(fbAuthSecretKey, 'thefad3@gmail.com', 'fsdf')","firebase = firebase.FirebaseApplication('https://flaskmvc.firebaseio.com/', auth)"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":43,"column":18},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":4},"end":{"row":45,"column":43},"action":"insert","lines":["        password = request.form['password']","        username = request.form['username']"]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":4},"end":{"row":45,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":8},"end":{"row":44,"column":12},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":44,"column":4},"end":{"row":44,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":47,"column":85},"end":{"row":48,"column":0},"action":"insert","lines":["",""]},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":45,"column":39},"end":{"row":46,"column":0},"action":"insert","lines":["",""]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":4},"end":{"row":48,"column":35},"action":"insert","lines":["        sha1 = hashlib.sha1()","        sha1.update(password)","        password = sha1.hexdigest()"]}]}],[{"group":"doc","deltas":[{"start":{"row":48,"column":4},"end":{"row":48,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":47,"column":4},"end":{"row":47,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":8},"end":{"row":46,"column":12},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":78},"end":{"row":49,"column":79},"action":"remove","lines":["'"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":77},"end":{"row":49,"column":78},"action":"remove","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":76},"end":{"row":49,"column":77},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":75},"end":{"row":49,"column":76},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":74},"end":{"row":49,"column":75},"action":"remove","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":73},"end":{"row":49,"column":74},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":72},"end":{"row":49,"column":73},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":71},"end":{"row":49,"column":72},"action":"remove","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":70},"end":{"row":49,"column":71},"action":"remove","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":69},"end":{"row":49,"column":70},"action":"remove","lines":["g"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":68},"end":{"row":49,"column":69},"action":"remove","lines":["@"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":67},"end":{"row":49,"column":68},"action":"remove","lines":["3"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":66},"end":{"row":49,"column":67},"action":"remove","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":65},"end":{"row":49,"column":66},"action":"remove","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":64},"end":{"row":49,"column":65},"action":"remove","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":63},"end":{"row":49,"column":64},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":62},"end":{"row":49,"column":63},"action":"remove","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":61},"end":{"row":49,"column":62},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":60},"end":{"row":49,"column":61},"action":"remove","lines":["'"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":60},"end":{"row":49,"column":61},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":61},"end":{"row":49,"column":62},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":62},"end":{"row":49,"column":63},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":63},"end":{"row":49,"column":64},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":60},"end":{"row":49,"column":64},"action":"remove","lines":["user"]},{"start":{"row":49,"column":60},"end":{"row":49,"column":64},"action":"insert","lines":["user"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":64},"end":{"row":49,"column":65},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":65},"end":{"row":49,"column":66},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":66},"end":{"row":49,"column":67},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":67},"end":{"row":49,"column":68},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":75},"end":{"row":49,"column":76},"action":"remove","lines":["'"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":74},"end":{"row":49,"column":75},"action":"remove","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":73},"end":{"row":49,"column":74},"action":"remove","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":72},"end":{"row":49,"column":73},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":71},"end":{"row":49,"column":72},"action":"remove","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":70},"end":{"row":49,"column":71},"action":"remove","lines":["'"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":70},"end":{"row":49,"column":71},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":71},"end":{"row":49,"column":72},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":72},"end":{"row":49,"column":73},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":73},"end":{"row":49,"column":74},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":74},"end":{"row":49,"column":75},"action":"insert","lines":["w"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":75},"end":{"row":49,"column":76},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":76},"end":{"row":49,"column":77},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":49,"column":77},"end":{"row":49,"column":78},"action":"insert","lines":["d"]}]}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":29,"column":27},"end":{"row":29,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1422500158760}