
def integer1():
 while True:
   try:
       integer1 = int(input("Enter a first number"))
       return integer1 
   except ValueError:
        print ("Invalid input")

def integer2():
 while True:
   try:
       integer2 = int(input("Enter a second number"))
       return integer2
   except ValueError:
        print ("Invalid input")       

a = integer1()
b = integer2()

def operation():
 while True:
    try:
     operator = input("Enter your operator")
     if operator == "+":
      return a+b
     elif operator == "-":
      return a-b
     elif operator == "*":
      return a*b
     elif operator == "/":
      return a/b
     else:
       raise TypeError("invalid operator")
    except TypeError:
     print("invalid Operator try other")
     

result = operation()
print(result)

