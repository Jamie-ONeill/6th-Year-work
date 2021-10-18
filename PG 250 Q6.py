#inputs

print("##########################################################")#line 2-9 are just to show a nice user interface
print("\t\t!FITinc Fitness Club!")
print("##########################################################")
print("\tHow can i help your today?please Choose an option:")
print("\t    Option 1:Add a member to the database ")
print("\t    Option 2.List all members in the database")
print("\t    Option 3.Exit")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

booking=int(input("\t    -"))#Asks the usesr which option they would like to pick

#process/outputs
if booking==3:
    print("##########################################################")
    print("\t\t!THANK YOU FOR USING FITINC FITNESS cLUB!")
    print("##########################################################")
  
elif booking==2:
    print("##########################################################")
    print("\t\t!WECLOME TO RYANAIR CREW MEMBER STATION!")
    print("##########################################################")
    crewtype=input("What type of crew member are you?(Pilot,Copilot,steward,stewardess)").capitalize()#user must pick an imput to continue,capitalize makes the first letter in the word always a capital
    if crewtype=="Pilot":
        hours=int(input("How many hours have you worked in total over the past two days?:"))
        hoursnew=int(input("How many hours will your current flight take?:"))
        hoursaverage=hours+hoursnew/2#divides the amout of hours by the last two days they have worked
        if hoursaverage<=8:#if 8 or under the pilot can fly and this code will run
            print("Thank you Pilot,Your are able to be apart of the cabin crew for this flight.")
        else:#if pilot works more then 8 hours this will run instead
            print("Aplogise Pilot,You are currently unabe to be apart of the cabin crew for this flight.")
            
    elif crewtype=="Copilot":
        crewhours=int(input("How many hours have you worked in total over the past two days?:"))
        crewhoursnew=int(input("How many hours will your current flight take?:"))
        crewhoursaverage=crewhours+crewhoursnew/2#divides the amout of hours by the last two days they have worked
        if crewhoursaverage<=10:#if 10 or under the Co-pilot can fly and this code will run
            print("Thank you Co-Pilot,Your are able to be apart of the cabin crew for this flight.")
        else:#if Co-Pilot works more then 10 hours this will run instead
            print("Aplogise Co-Pilot,You are currently unabe to be apart of the cabin crew for this flight.")
            
    elif crewtype=="Steward":
        crewhours=int(input("How many hours have you worked in total over the past two days?:"))
        crewhoursnew=int(input("How many hours will your current flight take?:"))
        crewhoursaverage=crewhours+crewhoursnew/2#divides the amout of hours by the last two days they have worked
        if crewhoursaverage<=12:#if 12 or under the Steward can fly and this code will run
            print("Thank you Steward,Your are able to be apart of the cabin crew for this flight.")
        else:#if steward works more then 12 hours this will run instead
            print("Aplogise Steward,You are currently unabe to be apart of the cabin crew for this flight.")

    elif crewtype=="Stewardess":
        crewhours=int(input("How many hours have you worked in total over the past two days?:"))
        crewhoursnew=int(input("How many hours will your current flight take?:"))
        crewhoursaverage=crewhours+crewhoursnew/2#divides the amout of hours by the last two days they have worked
        if crewhoursaverage<=12:#if 12 or under the Stewardess can fly and this code will run
            print("Thank you Stewardess,Your are able to be apart of the cabin crew for this flight.")
        else:#if stewardess works more then 12 hours this will run instead
            print("Aplogise Stewardess,You are currently unabe to be apart of the cabin crew for this flight.")
    else:
        print("Crew type not found,Please try again!")#if the user types in a crew member not on the list this message willl show

elif booking==1:
    name=input("What is your  first name?:").capitalize()
    surname = str(input("Waht is your surname:")).capitalize()#asks the users age and makes the first letter of there name a capitial
    age=int(input("What year were you born?(Full Year):"))#full year ex:1963
    weight = int(input("What is your weight in KG:"))
    bookinglist =[name,surname,age,weight]
    print("Your booking information:",bookinglist,)
    
    
    
        
else:#if the user puts in a number that is not 1,2 or 3 this code will run
    print("##########################################################")
    print("\t!UNRECOGNIZED NUMBER INPUTTED INTO TERMINAL!")
    print("##########################################################")
        
    
        


            

        
