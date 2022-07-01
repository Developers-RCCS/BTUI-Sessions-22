import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from sender import send_mail

#### REFERENCE ####
## https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/ ##

# Fetch the service account key JSON file contents
# Change the .json file below with your secrets file
cred = credentials.Certificate('hello-esp-99632-firebase-adminsdk-q5ofl-e4666f5f4e.json')
# Initialize the app with a service account, granting admin privileges
# Change the database URL below with your credentials
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://hello-esp-99632-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

_daytime = db.reference('Farm/daytime')

while True:
    if _daytime.get()['value'] == 1:
        send_mail()
