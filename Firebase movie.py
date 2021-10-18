from firebase import firebase
myDBconn = firebase.firebaseApplication("https//th-year-d3cd9-default-rtdb.firebaseio.com/",None)

movies =[]
scores = []

averagescore = sum(scores) /5


for i in range (0,5):
    movieinput =  str(input("movie name"))
    movies.append(movieinput)
    scoreinput = int(input("Movie score"))
    scores.append(scoreinput)
    


print("All chosen movies:", movies)
print("average off all movies:", averagescore)


myDBconn.post("/JamieOneill/patientInfo",movies, scores)
