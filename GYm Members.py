print("##########################################################")#line 2-9 are just to show a nice user interface
print("\t\t!FITinc Fitness Club!")
print("##########################################################")
print("\tHow can i help your today?please Choose an option:")
print("\t    Option 1:Add a member to the database ")
print("\t    Option 2.List all members in the database")
print("\t    Option 3.Exit")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

info = True
Memberslist =[]

while info == True:
    option = int(input("\t    -PLease pick an option"))
    if option == 1:
        name=input("What is your  first name?:").capitalize()
        surname = str(input("Waht is your surname:")).capitalize()#asks the users age and makes the first letter of there name a capitial
        age=int(input("What year were you born?(Full Year):"))#full year ex:1963
        weight = int(input("What is your weight in KG:"))
        bookinglist =[name,surname,age,weight]
        print("Your booking information:",bookinglist,)
        Memberslist.append(bookinglist)
    
    elif option == 2:
        print("The members of the database are:",Memberslist)
        
    elif option == 3:
        print("##########################################################")
        print("\t\t!THANK YOU FOR USING FITINC FITNESS CLUB!")
        print("##########################################################")
        info = False
    
    else:
        print("##########################################################")
        print("\t!UNRECOGNIZED NUMBER INPUTTED INTO TERMINAL!")
        print("##########################################################")
        info = False
        

        