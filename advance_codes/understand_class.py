class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name  # This stores the account owner's name
        self.balance = balance        # This stores the initial balance

    def show_balance(self):
        print(f"{self.owner_name} has a balance of {self.balance}.")
    
    def deposit(self,amount=0):
        self.balance = self.balance + amount
        print(f"new balance is: {self.balance}")


# Create an object of the class
account = BankAccount("Alice", 1000)  # Alice's account starts with $1000

# Call a method
account.show_balance()  # Output: Alice has a balance of 1000


account.deposit(200)

account.show_balance()