#Step 1: Enter Height and Weight of the Individaul
height  = float(input("Please Enter Your Height in CM: "))
weight = float(input("Please Enter Your Weight in KG: "))


#Start the formula for the BMI
height = height/100
BMI = weight /(height*height)

#classification of BMI

if BMI <= 18.5:
    print("You are Under weight")

elif BMI <= 24.9:
    print("You are Normal weight")
elif BMI <= 29.9:
    print("You are Overweight")
elif BMI <= 34.9:
    print("You are Obesity(Class I)")
elif  BMI <= 39.9:
    print("You are Obesity(Class II)")
elif BMI > 40:
    print("You are serverly Overweight")
else:
    print("Please Enter Valid Details")


