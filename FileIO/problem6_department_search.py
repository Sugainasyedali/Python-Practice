import csv
department = input("Enter your dept")
with open("FileIO\students.csv","r") as file:
 reader = csv.DictReader(file)
 for student in reader:
        if student["department"] == department:
             print(student["name"])