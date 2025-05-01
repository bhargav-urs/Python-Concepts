class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Public variable
        self._account_type = "Savings"  # Protected variable
        self.__account_number = "1234567890"  # Private variable

    # Public method to access balance (encapsulation)
    def get_balance(self):
        return self.balance

    # Public method to deposit money (encapsulation)
    def deposit(self, amount):
        self.balance += amount

    # Public method to access private variable through encapsulation
    def get_account_number(self):
        return self.__account_number

# Create an instance of BankAccount
account = BankAccount(1000)
print("Public variable (balance):", account.balance)
print("Protected variable (_account_type):", account._account_type)

# Accessing private variable directly will raise an error
# print(account.__account_number)  # Uncommenting this will cause an AttributeError

# Accessing private variable via public method
print("Private variable (account number):", account.get_account_number())


account.deposit(500) # Using the deposit method to add money
account.balance += 500 # Directly accessing the public variable
print("Updated balance after deposit:", account.get_balance())