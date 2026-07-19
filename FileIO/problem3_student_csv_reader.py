import csv
with open("FileIO/students.csv") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(student)