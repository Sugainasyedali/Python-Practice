print("ATM MENU 1.Balance 2.deposit 3.withdrawl 4.Exit")
choice =int(input("Enter Your Choice"))
initialAmount = 10000
minimumbalance =5000
if choice ==1:
    print(initialAmount)
elif choice==2:
   deposit= int(input("Enter Your Deposit Amount"))
   newBalance = initialAmount + deposit
   print(newBalance)
elif choice==3:
    withdrawl =int(input("Enter Your withdrawl Amount"))
    balance = initialAmount - withdrawl
    if withdrawl >= balance :
        print("withdrawl successfull : " ,balance)
    else:
        print("Insufficient Balance")
else:
    print("Exit")