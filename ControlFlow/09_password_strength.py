password =input("Enter your password")
passwordlen = len(password)
hasUpper =False
haslower = False
hasdigit =False
for ch in password:
    if ch.isupper():
        hasUpper = True
    if ch.islower():
        haslower = True
    if ch.isdigit():
        hasdigit = True
    
if passwordlen>8 and hasUpper and haslower and hasdigit:
    print("Strong Password")
elif hasUpper and hasdigit and passwordlen>8:
    print("Medium Password")
elif hasUpper or haslower or hasdigit or passwordlen>8:
    print("Weak Password")
else:
    print("password requirement doesn't match")