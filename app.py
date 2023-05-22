from flask import Flask, redirect, url_for, request, render_template,session
app = Flask(__name__)
import pyrebase

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
app.secret_key = 'unsecreto'

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == 'POST':
        if request.form["LoginButton"] == "Login":
           return redirect(url_for('login'))
           #return render_template('login.html')
        else:
           return redirect(url_for('login'))
           #return render_template('login.html')
    else:
       return render_template('index.html')
   

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if('user' in session):
        #return 'Hi,{}'.format(session['user'])
        file = open('votelog.txt','r')
        for x in file: #ver si el email esta en el archivo
            if x == email:
                file.close()
                return redirect(url_for('teamsNoVoting'))
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
                file = open('votelog.txt','r')
                for x in file: #ver si el email esta en el archivo
                    if x == email:
                        file.close()
                        return redirect(url_for('teamsNoVoting'))
                file.close()
                return redirect(url_for('teams'))
                #print(user)
            except:
                return 'Failed to Login'
            # if email is not in database
                #   return message 'no estas registrado'
            # si esta registrado login y mandarlo a pagina votacion
                # si no voto dejarlo votar
                # si ya voto solo mostrar los resultados que se van actualizando.               
            return render_template('login.html')
    else:
      return render_template('login.html')

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
                    return 'Failed to Register'
            return render_template('register.html')
   else:
        return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/teams',methods = ['POST', 'GET'])
def teams():
    return render_template('teams.html')

@app.route('/votingresults')
def teamsNoVoting():
    return render_template('/teamsNoVoting')

if __name__ == '__main__':
   app.run(debug = True)