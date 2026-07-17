numbers = (45,78,12,98,56)
currentmax = numbers[0]
for i in numbers:
   if i > currentmax:
        currentmax = i
print("MAXIMUM:",currentmax)
currentmin = numbers[0]
for i in numbers:
    if i < currentmin:
        currentmin =i
print("MINIMUM:",currentmin)
    

    