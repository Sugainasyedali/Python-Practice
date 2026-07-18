Student ={
    "Sugaina":98,
    "Ali":99,
    "Virat":100,
    "Rohit":100,
    "Msd":100
}
name=input("Enter Student name")
try:
   print(Student[name])
except KeyError:
   print("Student not found")