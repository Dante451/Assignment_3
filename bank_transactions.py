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
locale.setlocale(locale.LC_ALL, '')
#locale is an imported module that allows you to easily format numbers and data according to your region standards
#LC_ALL means use all locale settings for formatting. In this case, it is using the North American formatting
def deposit_protocol(balance):
    transaction_input = float(input("Enter amount of transaction: "))
    balance += transaction_input
    print("*" * 40)
    print(f'{"Successfully deposited funds": ^40}')
    print("   Your current balance is:", locale.currency(balance, grouping = True))
    print("*" * 40)
    return balance
#This function can add money to the current balance when called
def withdraw_protocol(balance):
    transaction_input = float(input("Enter amount of transaction: "))
    if transaction_input > balance:
        print("*" * 40)
        print(f'{"insufficient funds": ^40}')
        print("*" * 40)
    else:
        balance -= transaction_input
        print("*" * 40)
        print(f'{"Successfully withdrew funds": ^40}')
        print("   Your current balance is:", locale.currency(balance, grouping = True))
        print("*" * 40)
    return balance
#This function removes money from the current balance when called,
#and has an if/else check to make sure you don't withdraw more than is available 
def invalid_protocol():
    print("*" * 40)
    print(f'{"Invalid selection": ^40}')
    print("*" * 40)
#This function displays a message when anything other than D, W, Q is entered 
while True:
    print("*" * 40)
    print(f'{"PIXELL RIVER FINANCIAL" : ^40}')
    print(f'{"ATM Simulator" : ^40}')
    print("  Your Current Balance Is:", locale.currency(balance, grouping = True))
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
#This loop prints off an updating main menu with the current balance 
#and acceptable selection options, then has a simple if/else statement
#that calls the appropriate function to change the user's balance
#and wipes the screen after three seconds 