
class Bank:


    def __init__(self, available_Balance):

        self.available_Balance = available_Balance
        self.amt_withdraw = 0

    def bank_transactions(self):
        if self.amt_withdraw>self.available_Balance:
            return "Insufficient Funds"
        else:
            self.available_balance = self.available_Balance - self.amt_withdraw

            return f"Collect your cash...\nNow Available balance {self.available_balance}"

    def amount_withdraw(self):
        self.amt_withdraw = int(input("Please enter the amount - "))


        print(self.bank_transactions())



obj1 = Bank(49999.99)

obj1.amount_withdraw()






