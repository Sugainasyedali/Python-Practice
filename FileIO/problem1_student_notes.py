with open("FileIO/notes.txt","r") as file:
    data = file.read()
    print(data.rstrip())