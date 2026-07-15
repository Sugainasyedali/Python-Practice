print("signal color  1.red 2.green 3.yellow")
user = int(input("Enter your signal color in number"))
if user==1:
    print("stop")
elif user==3:
    print("ready")
elif user==2:
    print("go")
else:
    print('Invalid Signal Number')