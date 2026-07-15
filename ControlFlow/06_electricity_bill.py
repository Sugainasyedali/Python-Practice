Units =int(input("Enter Your Units"))
if Units>=0 and Units<=100:
    print("The Electricity Bill is 0 rupees")
elif Units >=101 and Units <=200:
    bill =Units*2
    print(f"The Electricity Bill is {bill} rupees")
elif Units>=201 and Units <=500:
    bill =Units*5
    print(f"The Electricity Bill is {bill} rupees")
else:
    bill = Units*8
    print(f"The Electricity Bill is {bill} rupees")