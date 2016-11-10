import sys
import json
import time


# It open and read the data in the json file
Data = open("C:\Users\FESTUS\Documents/bootcamp11\mathematics_library.json").read()
QUIZ = json.loads(Data)
print QUIZ

from firebase import firebase
firebase = firebase.FirebaseApplication('https://quiz-app-e9563.firebaseio.com/')
result = firebase.post('/',QUIZ)