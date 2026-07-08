class BankBalance:
    def __init__(self, balance):
        self.__balance = balance

    def myBalance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful. New balance is:", self.__balance)
        else:
            print("Deposit amount must be positive.") 
    

kiran = BankBalance(1000) 
kiran.deposit(500)
print("My balance is:", kiran.myBalance()) 