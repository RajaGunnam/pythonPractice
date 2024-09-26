
class Bank:


    def __init__(self, available_Balance):

        self.available_Balance = available_Balance
        self.amt_withdraw = 0

    def bank_transactions(self):
        if self.amt_withdraw>self.available_Balance:
            return "Insufficient Funds"
        else:
            self.available_balance = self.available_Balance - self.amt_withdraw

            return f"Please collect your cash...\nNow Available balance {self.available_balance}"

    def amount_withdraw(self):
        self.amt_withdraw = float(input("Please enter the amount - "))


        print(self.bank_transactions())



bank_obj1 = Bank(49999.99)



class EMI_Deductions(Bank):

    def __init__(self, available_Balance, principle_amount, interest, monthlyEMI):
        super().__init__(available_Balance)
        self.interest = interest
        self.monthlyEMI = monthlyEMI

    def house_Loan_emi_deduction(self):
        if self.available_Balance<=self.monthlyEMI:
            return "Please add funds to your account to avoid penalties"
        else:
            self.available_Balance =self.available_Balance - self.monthlyEMI
            return f"The house loan EMI of {self.monthlyEMI} has been deducted from your account.\nThank you\nXYZ Bank"


# Create an instance of Bank and make a withdrawal
bank_obj1 = Bank(49999.99)
bank_obj1.amount_withdraw()

# Create an instance of EMI_Deductions and deduct EMI
hL_obj1 = EMI_Deductions(available_Balance=49999.99, principle_amount=2000000, interest=8.7, monthlyEMI=12735)
print(hL_obj1.house_Loan_emi_deduction())


















