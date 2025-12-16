class account:
    def __init__(self,accountnumber):
        self.accountnumber=accountnumber
        self._balance=4000
        self._pin=3333
        self._customer_id=7878787

    def withdrawl(self,userinput,pin):
        if pin==self._pin:
            data=self._balance-userinput
            if data > 0:
                self._balance=data
                print(f"Withdraw successful: {userinput}")
            else:
                print("Insufficient balance!")
        else:
            print("Please enter valid pin")

    def deposit(self,amount,pin):
        if pin==self._pin:
            if amount > 0:
                self._balance+=amount
                print(f"Deposit successful: {amount}")
            else:
                print("Deposit amount must be positive")
        else:
            print("Please enter valid pin")
    def check_balance(self):
        print(f"Current balance: {self._balance}")


acc=account(1)

acc.deposit(500,3333)
acc.check_balance()

acc.withdrawl(300,3333)
acc.check_balance()
