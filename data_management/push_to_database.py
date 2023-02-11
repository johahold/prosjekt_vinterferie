import firebase_admin
from firebase_admin import credentials
from firebase_admin import db




cred = credentials.Certificate("vinterprosjekt-it2-firebase-adminsdk-wi0bg-f0efd8881e.json")
firebase_admin.initialize_app(cred, {'databaseURL':"https://vinterprosjekt-it2-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference("/")
