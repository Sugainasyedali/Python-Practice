inventory ={
    "pen":10,
    "Book":5,
    "Pencil":20
}
inventory["pen"] = 15
del inventory["Pencil"]
for key,value in inventory.items():
    print(key,value)