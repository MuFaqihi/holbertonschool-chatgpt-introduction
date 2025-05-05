#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        # Initialize the balance to 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Deposit the specified amount into the balance
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Withdraw the specified amount from the balance
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Print the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()  # Create a new Checkbook instance
    while True:
        # Get user input for the action they want to perform
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        # Exit the loop if the user types 'exit'
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                # Ask for deposit amount and attempt to convert it to a float
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit amount.")
        elif action.lower() == 'withdraw':
            try:
                # Ask for withdrawal amount and attempt to convert it to a float
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
