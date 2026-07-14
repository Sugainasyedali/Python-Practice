principal = int(input("Enter your principal amount "))
rate = int(input("Enter your rate percentage "))
time =int(input("Enter your year of time "))
SI = (principal*rate*time)/100
print(SI)
FinalAmount = principal+SI
print(FinalAmount)