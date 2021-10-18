def BMI(HeightIn, WeightIn):
    Heightcal = Height /100
    bodymass = Weight / (Heightcal**2)
    return (bodymass)
    
Height = float(input("How tall are you cm's:"))
Weight = float(input("What is your weight in kilograms;"))

bodymasscalculator = BMI(HeightIn = Height, WeightIn = Weight)

if bodymasscalculator < 18.5:
    print("Underweight")

elif bodymasscalculator >= 18.5 and bodymasscalculator<= 24.9:
    print("Normal")
    
elif bodymasscalculator >= 25 and bodymasscalculator <=29.9:
    print("Overweight")

else :
    print("YOur fat")
    
    
print(bodymasscalculator)



    