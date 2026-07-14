#Largest of three
x=int(input("Enter Your First Number"))
y=int(input("Enter Your Second Number"))
z=int(input("Enter Your Third Number"))
#Logic to find largest of three
if x>y and x>z:
    print("X is the Largest")
elif y>z and y>x :
    print("Y is the Largest")
else:
    print("Z is the Largest")