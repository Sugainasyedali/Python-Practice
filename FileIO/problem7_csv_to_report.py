import csv
with open("FileIO\students.csv","r") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(student)
with open("FileIO\\report.txt","w") as file:
    file.write("Student Report\n")
    file.write("Name : Sugaina\n")
    file.write("Department : AIDS\n")
    file.write("CGPA : 8.5\n")

    