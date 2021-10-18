from firebase import firebase

myDBconn = firebase.FirebaseApplication("https://th-year-d3cd9-default-rtdb.firebaseio.com/", None)

myGetResults = myDBconn.get('/JamieOneill/patientInfo/',None)

for keyID in myGetResults:
    print(keyID, "\t", myGetResults [keyID]['name'], "\t", myGetResults[keyID]['age'])
    