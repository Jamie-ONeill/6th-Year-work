def thermostatmodel1 (actualIn, targetIn):
    if actual < target:
        return 1
    
    elif actual == target:
        print("There is no need to turn on the heating")
        
    
    else:
        return 0
    
    
    
actual = int(input("Room Temp:"))
target = int(input("Target temp:"))

actualtemp = thermostatmodel1( actualIn = actual, targetIn = target)
print(actualtemp)