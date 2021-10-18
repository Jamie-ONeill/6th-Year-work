from firebase import firebase
myDBConn = firebase.FirebaseApplication("https://th-year-d3cd9-default-rtdb.firebaseio.com/",None)





moviename = []
moviescore = []


for i in range(0,5):
    ele = input("Enter movie name:")
    movs = int(input("Enter score for movie:"))
 
    moviename.append(ele)
    moviescore.append(movs)
   
   
data = {
    "moviename": moviename,
    "moviescore": moviescore,
    }

myDBConn.post("/subhanfazal/movie",data)

myGetResults = myDBConn.get('/subhanfazal/movie', None)


"""
for keyID in myGetResults:
    print(keyID, "\t", myGetResults[keyID]['moviename'], "\t",myGetResults[keyID]['moviescore'])
"""    

# Printing average of the list
average = sum(moviescore) / len(moviescore)
print("Average list", average)
 
print(moviename, moviescore)

"""
def linearSearch(listIn, keyIn):
    for index in range(len(listIn)):
        if listIn[index] == keyIn:
            return index
    return -1


movieslotname = print(linearSearch(moviename, max(moviename)))
moviescoreslot = print(linearSearch(moviescore, max(moviescore)))

indexHighestScore = linearSearch(moviename, max(moviename))

print(indexHighestScore )
"""