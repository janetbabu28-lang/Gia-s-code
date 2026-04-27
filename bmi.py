height = float(input("Please enter your height in cm: "))
weight = float(input("Please enter your weight in kg: "))

bmi = weight / (height/100)**2

if bmi <18.5:
    print("Your are underweight")
elif  bmi <24.9:
    print("Your are acceptable weight")  
elif  bmi <29.9:
    print("Your are overweight") 
elif  bmi <39.9:
    print("Your are severly overweight")
else:
    print("You are obese.")             
