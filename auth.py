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

email = "test@gmail.com"
password = "12345678"

#user= auth.create_user_with_email_and_password(email,password)

#user = auth.sign_in_with_email_and_password(email,password)

#info = auth.get_account_info(user['idToken'])
print(info)

#auth.send_email_verification(user['idToken'])