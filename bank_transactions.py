"""
Description: Bank transactions file for assignment 3
Author: Dante Daciuk
Date: 7/2/24
"""
#Note: My code looks very different from previous versions because there was too many problems, so I wiped it and restarted
import random
import locale
import os
from time import sleep

random_balance = random.randint(-1000, 10000)
balance = round(random_balance, 2)

def deposit_protocol(balance):
    transaction_input = float(input("Enter amount of transaction: "))
    balance += transaction_input
    print("*" * 40)
    print("Successfully deposited funds")
    print("Your current balance is: ", balance)
    return balance

def withdraw_protocol(balance):
    transaction_input = float(input("Enter amount of transaction: "))
    if transaction_input > balance:
        print("*" * 40)
        print("insufficient funds")
    else:
        balance -= transaction_input
        print("*" * 40)
        print("Successfully withdrew funds")
        print("Your current balance is: ", balance)
    return balance

def invalid_protocol():
    print(f'{"Invalid selection": ^40}')
    print("*" * 40)

while True:
    print("*" * 40)
    print(f'{"PIXELL RIVER FINANCIAL" : ^40}')
    print(f'{"ATM Simulator" : ^40}')
    print("  Your Current Balance Is:", balance)
    print("")
    print(f'{"Deposit: D" : ^40}')
    print(f'{"Withdraw: W" : ^40}')
    print(f'{"Quit: Q" : ^40}')
    print("*" * 40)
    transaction_selection = input("Enter your selection: ").upper()
    if transaction_selection == "D":
        balance = deposit_protocol(balance)
    elif transaction_selection == "W":
            balance = withdraw_protocol(balance)
    elif transaction_selection == "Q":
        print("Goodbye")
        break
    else:
        invalid_protocol()
    sleep(3)
    os.system("cls" if os.name == "nt" else "clear")