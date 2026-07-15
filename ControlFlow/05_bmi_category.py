weight = int(input("Enter your weight in kg"))
height = float(input("Enter your height in meters"))
BMI = weight /(height*height)
print(f"BMI: {round(BMI, 2)}")
if BMI <18.5:
    print("Underweight")
elif BMI >=18.5 and BMI <=24.9:
    print("Normal Weight")
elif BMI >= 25.0 and BMI <=29.9:
    print("Overweight")
else:
    print("Obese")
    