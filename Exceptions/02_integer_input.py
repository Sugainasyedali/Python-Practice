
while True:
    try:
       integer = int(input("Enter an integer"))
       print(integer) 
       break
    except ValueError:
        print ("Invalid input")