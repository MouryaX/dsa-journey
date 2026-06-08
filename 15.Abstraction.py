
class account:
    def __init__ (self, balance, acc_no):
        self.balance  = balance
        self.acc_no = acc_no
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"Was Credited")
        print("Balance:",self.get_balance()) 
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"Was Debited")
        print("Balance:", self.get_balance())
        
    def get_balance(self):
        return self.balance
    
c1 = account(3400000,112)
print(c1.balance)
c1.debit(40000)
c1.credit(560000)


