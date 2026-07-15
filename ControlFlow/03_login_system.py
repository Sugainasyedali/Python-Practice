Username = "admin"
Password = "python123"
User =input("Enter Your Username")
UserPassword = input("Enter Your Password")
if User==Username and Password==UserPassword:
    print("Login Successful")
elif Password!=UserPassword and User!=Username :
    print("Wrong Password and Username")
elif User!=Username:
    print("User Not Found")
else:
    print("Wrong Password")