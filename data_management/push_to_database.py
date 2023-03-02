import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import json
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
            
cred = credentials.Certificate("vinterprosjekt-it2-firebase-adminsdk-wi0bg-f0efd8881e.json")
firebase_admin.initialize_app(cred, {'databaseURL':"https://vinterprosjekt-it2-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference("/bazaar")

with open("bazaar_info.json", "r") as f:
	file_contents = json.load(f)
# ref.set(file_contents)

ref.child(dt_string).set(file_contents)

os.remove("bazaar_info.json")

ref = db.reference("/auctions")

with open("auctions_info.json", "r") as f:
	file_contents = json.load(f)
# ref.set(file_contents)

ref.child(dt_string).set(file_contents)

os.remove("auctions_info.json")

# data_push = ref.push().set(file_contents)

# post_id = data_push.key
