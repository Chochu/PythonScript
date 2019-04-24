## Wanmin Zhang
## ITM 313
## Professor Hawkins
## bankclass.py

## Checking Account class
class checkingAcc:
    ##Store acctBalance when the object is created
    _accBalance = 0

    def __init(self, accBalance):
        ## Starting balance is $500
        self._accBalance = accBalance

    ## Account balance
    def viewBal(self):
        return self._accBalance


    def interestAccrued(self):
        interest = 0.1
        years = 1
        intAccrued = self._accBalance * interest * years
        return str(intAccrued)

    ## Withdraw function
    def withdraw(self):
        ## Asking user to enter withdraw $$$
        withdrawAmt = int(input("Please enter how much you would like to withdraw: "))
        ## Checking to ensure they're not withdrawing more than what they have
        if self._accBalance < withdrawAmt:
            print("Sorry, you have insufficient funds.")
            input("Type 'E' to exit or 'M' for menu.")
        ## Checking that they're not withdrawing a negative amount of $
        elif withdrawAmt < 0:
            print("Negative entries are not allowed. Please try again.")
            input("Type '5' to exit or '0' for menu.")
        ## If all else is good, subtract withdraw amount from balance
        else:
            self._accBalance -= withdrawAmt
            ## Printing out withdraw, balance, and interest info for user
            print("You current balance is: " + str(self._accBalance))
            print("Your interest accrued is:" + self.interestAccrued())

    ## Deposit function
    def deposit(self):
        ## Asking user to enter deposit $$$
        depositAmt = int(input("Please enter how much you would like to deposit: "))
        #need to convert deposit to int type
        self._accBalance += depositAmt ## Calculating the balance w/ deposit
        ## Printing out deposit, balance, and interest info for user
        print("You have deposited" + str(depositAmt) + "into your account.")
        print("Your current balance is: " + str(self._accBalance))
        print("Your interest accrued is:" + self.interestAccrued())
