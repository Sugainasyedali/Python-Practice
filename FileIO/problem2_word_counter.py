filename = input("Enter file name")
with open(filename ,"r") as file:
     data =file.read()
     print(len(data))
     word = data.split()
     print(len(word))
     line = data.split("\n")
     print(len(line))
     