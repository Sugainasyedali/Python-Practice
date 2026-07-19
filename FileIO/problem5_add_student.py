import csv
name = input("Enter a name")
department = input("Enter your dept")
cgpa = input("Enter your cgpa")
with open("FileIO\students.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,department,cgpa])
    print("Student added successfully!")
