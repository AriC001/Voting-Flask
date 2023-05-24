from flask import Flask, redirect, url_for, request, render_template,session
from flask_socketio import SocketIO,emit
# from flask_sock import Sock
from threading import Lock
import pyrebase
import json

app = Flask(__name__)
app.secret_key = 'unsecreto'
socketio= SocketIO(app)
# sock = Sock(app)

config={
    'apiKey': "AIzaSyAyMHVwRqWi1f_EVR9UB6_iYQ75tNXpbs8",
    'authDomain': "pythonauth-001.firebaseapp.com",
    'projectId': "pythonauth-001",
    'storageBucket': "pythonauth-001.appspot.com",
    'messagingSenderId': "731275789532",
    'appId': "1:731275789532:web:a22f685f6927531a946019",
    'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

thread = None
tread_lock = Lock()

votos = []
@socketio.on('connect')
def ws_connect():
    votos.clear()
    f = open('results.json','r')
    jsonData = json.load(f)
    f.close()
    for i in jsonData:
        votos.append(jsonData[i])
    emit('votos',votos,broadcast=True)

# votos = []
# @sock.route('/echo')
# def echo(ws):
#     while True:
#         #data=ws.receive()
#         votos.clear()
#         f = open('results.json','r')
#         jsonData = json.load(f)
#         f.close()
#         for i in jsonData:
#             votos.append(jsonData[i])
#         ws.send(votos)

# votos = []
# def votingUpdate():
#     while True:
#         votos.clear()
#         f = open('results.json','r')
#         jsonData = json.load(f)
#         f.close()
#         for i in jsonData:
#             votos.append(jsonData[i])
#         socketio.emit('votos',votos)
#         socketio.sleep(1)

@app.route('/',methods=["GET","POST"])
def index():
    option = 'login'
    f = open('results.json','r')
    jsonData = json.load(f)
    f.close()
    votos = []
    for i in jsonData:
        votos.append(jsonData[i])
    if('user' in session):
        option = 'logout'
    if request.method == 'POST':
        if request.form["LoginButton"] == "Login":
           return redirect(url_for('login'))
           #return render_template('login.html')
        else:
           return redirect(url_for('login'))
           #return render_template('login.html')
    else:
       return render_template('index.html',votos=votos,option=option)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if('user' in session):
        email = session['user']
        #return 'Hi,{}'.format(session['user'])
        # file = open('votelog.txt','r')
        with open('votelog.txt', 'r') as file:
            content = file.read()
            if email in content:
                return redirect('login')
        file.close()
        return redirect(url_for('teams'))
    if request.method == 'POST':
        if request.form["LogIn/Register"] == "Go Register":
            return redirect(url_for('register'))
        else:
            email = request.form['emailuser']
            password = request.form['password']
            try:
                user = auth.sign_in_with_email_and_password(email,password)
                session['user'] = email
                email = session['user']
                #return 'Hi,{}'.format(session['user'])
                # file = open('votelog.txt','r')
                with open('votelog.txt', 'r') as file:
                    content = file.read()
                    if email in content:
                        file.close()
                        return redirect('/')
                return redirect(url_for('teams'))
                #print(user)
            except:
                return render_template('login.html',displayProp='block')
            # if email is not in database
                #   return message 'no estas registrado'
            # si esta registrado login y mandarlo a pagina votacion
                # si no voto dejarlo votar
                # si ya voto solo mostrar los resultados que se van actualizando.               
            return render_template('login.html')
    else:
      return render_template('login.html',displayProp='none')

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
        if request.form["LogIn/Register"] == "Go LogIn":
            return redirect(url_for('login'))
        else:
            email = request.form['email']
            password = request.form['password']
            password2 = request.form['passwordConfirm']
            if password == password2:
                try:
                    user = auth.create_user_with_email_and_password(email,password)
                    session['user'] = email
                    return redirect(url_for('teams'))
                except:
                    return render_template('register.html',displayProp='block')
            else:
                return render_template('register.html',displayProp='noMatch')
            # return render_template('register.html')
   else:
        return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/teams',methods = ['POST', 'GET'])
def teams():
    if request.method == 'POST':
        file = open('votelog.txt','a')
        email = session['user']
        file.write(email+'\n')
        file.close()
        if request.form["Equipo"] == "BOCA":
            with open('results.json') as f:
                data = json.load(f)
            for valor in data:
                if valor =='Boca':
                    data[valor] = data[valor] + 1
            with open('results.json', 'w') as f:
                json.dump(data, f)
        elif request.form["Equipo"] == "RIVER":
            with open('results.json') as f:
                data = json.load(f)
            for valor in data:
                if valor == 'River':
                    data[valor] = data[valor] + 1
            with open('results.json', 'w') as f:
                json.dump(data, f)
        elif request.form["Equipo"] == "INDEPENDIENTE":
            with open('results.json') as f:
                data = json.load(f)
            for valor in data:
                if valor == 'Independiente':
                    data[valor] = data[valor] + 1
            with open('results.json', 'w') as f:
                json.dump(data, f)
        elif request.form["Equipo"] == "TOMBA":
            with open('results.json') as f:
                data = json.load(f)
            for valor in data:
                if valor == 'Tomba':
                    data[valor] = data[valor] + 1
            with open('results.json', 'w') as f:
                json.dump(data, f)
        # f = open('results.json','r')
        # jsonData = json.load(f)
        # f.close()
        # votos = []
        # for i in jsonData:
        #     votos.append(jsonData[i])
        return redirect('/')

    f = open('results.json','r')
    jsonData = json.load(f)
    f.close()
    votos = []
    for i in jsonData:
        votos.append(jsonData[i])
    return render_template('teams.html',votos = votos)

@app.route('/votingresults')
def teamsNoVoting():
    return render_template('/teamsNoVoting')

if __name__ == '__main__':
    # socketio.run(app)
    # thread1 = threading.Thread(target=votingUpdate(),daemon=True)
    # thread1.start()
    app.run(host="0.0.0.0",port=5000, debug = True)