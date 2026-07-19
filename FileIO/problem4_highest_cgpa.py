import csv 
with open("FileIO/students.csv") as file:
     reader = csv.DictReader(file)
     list =[]
     for line in sorted(reader,key=lambda reader:reader["cgpa"]):
        list.append(line)
     print(list[2])