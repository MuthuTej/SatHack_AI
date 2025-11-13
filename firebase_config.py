import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")  # from Firebase Console
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sathack-7d9d8-default-rtdb.firebaseio.com/'
})

database = db
