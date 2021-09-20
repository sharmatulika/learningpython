print("This exercise calculates the BMI of a person")
weight=float(input("Enter your weight in kg"))
height=float(input("Enter your height in meters"))
bmi=round(weight/(height**2),2)
print("The bmi is ",bmi)
if(bmi<=18.5):
    print("The classification is Underweight")
elif (bmi>18.5 and bmi<=24.9):
     print("The classification is Normal weight")
elif(bmi>24.9 and bmi<=29.9):
     print("The classification is Overweight")
else:
     print("The classification is Obesity")
