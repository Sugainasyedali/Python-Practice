marks =int(input("Enter Your Marks"))
if marks >=90:
    print("You have got \"A\" grade")
elif marks >=80 and marks <=89:
    print("You have got \"B\" grade")
elif marks >=70 and marks<=79:
    print("You have got \"C\" grade")
elif marks>=50 and marks<=69:
    print("You have got \"D\" grade")
else:
    print("You Failed")