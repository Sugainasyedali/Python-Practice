import re
email = input("enter your email")
if re.fullmatch(r"^\w+@\w+\.com$",email):
    print("Valid Email")
else:
    print("Invalid Email")