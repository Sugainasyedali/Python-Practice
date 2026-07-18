numbers=[10,20,30]
index = int(input("Enter an index"))
try:
    print(numbers[index])
except IndexError:
    print("Invalid index")