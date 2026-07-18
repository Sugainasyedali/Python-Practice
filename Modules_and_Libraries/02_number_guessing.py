import random
number = random.randint(1,50)
while True:
    guess = int(input("enter a number"))
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
         print("Hurray you got it")
         break