from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

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
    if request.method == 'POST':
        if request.form["LogIn/Register"] == "Go Register":
            return redirect(url_for('register'))
        else:
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
            return render_template('register.html')
   else:
        return render_template('register.html')

if __name__ == '__main__':
   app.run(debug = True)