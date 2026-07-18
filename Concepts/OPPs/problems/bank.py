class Bank:
    bank_name = "State Bank of India"

    def __init__(self, balance, account_no):
        self.__balance = balance
        self.__account_no = account_no

    # Deposit
    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Rs. {amount} credited successfully. New balance: Rs. {self.__balance}"
        return "Credit amount must be positive."

    # Withdraw
    def debit(self, amount):
        if amount > self.__balance:
            return f"Insufficient balance. Current balance: Rs. {self.__balance}"

        self.__balance -= amount
        return f"Rs. {amount} debited successfully. New balance: Rs. {self.__balance}"

    # Check Balance
    def get_balance(self):
        return f"Account No: {self.__account_no}, Balance: Rs. {self.__balance}"


# Create an account
manu = Bank(1000, 123456789)

print(manu.get_balance())
print(manu.credit(1500))
print(manu.debit(500))
print(manu.get_balance())