from firebase import firebase
myDBconn = firebase.FirebaseApplication("https://th-year-d3cd9-default-rtdb.firebaseio.com/", None)

data ={
    "name":"Jamie",
    "age":17,
    }

myDBconn.post("/JamieOneill/patientInfo",data)