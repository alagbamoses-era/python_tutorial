#!/usr/bin/python3


class ATM:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder #private attribute
        self.__balance = initial_balance # private attribute

    # Getter for balance (only to view balance)
    @property
    def balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited ${amount}. New balance: ${self.__balance}')
        else:
            print('Deposit amount must be positive.')
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f'Withdraw ${amount}. New balance: ${self.__balance}')
            else:
                print('Insufficient balance')
        else:
            print('Withdrawal amount must be positive')

    # Mthod to display account info
    def account_info(self):
        print(f'Account Holder: {self.__account_holder}')
        print(f'Current Balance: ${self.__balance}')

# usage
atm = ATM('Alice', 1000)

# Display account info
atm.account_info()

# Deposit money
atm.deposit(500)

# Withdraw money
atm.withdraw(300)

# Try to withdraw more than available
atm.withdraw(2000)


# Display balance using property
print(f'Final Balance: ${atm.balance}')


