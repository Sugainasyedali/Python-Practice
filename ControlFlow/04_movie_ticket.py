age = int(input("Enter Your Age"))
# Movie Ticket Pricing 
if age<=5:
    print("Free Ticket")
elif age >5 and age <=18:
    print("Ticket price 150")
else:
    print("Ticket price 200")