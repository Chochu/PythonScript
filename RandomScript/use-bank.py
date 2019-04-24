import bankclass

## Wanmin Zhang
## ITM 313
## Professor Hawkins
## use-bank.py

b = bankclass.checkingAcc()

print("Hello! Welcome to the Bank for Broke People!")
print("Enter '1' to view your account balance.")
print("Enter '2' to withdraw money from your bank account.")
print("Enter '3' to deposit money into your bank account.")
print("Enter '4' to view how much interest you have accrued.")
print("Enter '5' to exit.")
print("Enter '0' to go back to the menu.")
user = input("Please choose an option from our menu: ")

while(user != 5):
    if int(user) == 0:
        print("Hello! Welcome to the Bank for Broke People!")
        print("Enter '1' to view your account balance.")
        print("Enter '2' to withdraw money from your bank account.")
        print("Enter '3' to deposit money into your bank account.")
        print("Enter '4' to view how much interest you have accrued.")
        print("Enter '5' to exit.")
        print("Enter '0' to go back to the menu.")
        user = int(input("Please choose an option from our menu: "))
    elif int(user) == 1:
        print(b.viewBal())
        user = 0; ##Reset user input to print out menu
    elif int(user) == 2:
        print(b.withdraw())
        user = 0; ##Reset user input to print out menu
    elif int(user) == 3:
        print(b.deposit())
        user = 0; ##Reset user input to print out menu
    elif int(user) == 4:
        print(b.interestAccrued())
        user = 0; ##Reset user input to print out menu
    else:
        print("Exiting...")
        exit()
