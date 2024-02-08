"""
Description: Bank transactions file for assignment 3
Author: Dante Daciuk
Date: 7/2/24
"""
import random
import locale
import os
#I placed all imported modules above the code so I know what is active and what is not

interface = {"D", "W", "Q"}
balance = random.randint(-1000, 10000)
deci_balance = float(balance)
locale.setlocale(locale.LC_ALL, '')
#This code creates a random initial balance and sets the locale currency to my default settings (English)

print("****************************************")
print(f'{"PIXELL RIVER FINANCIAL" : ^40}')
print(f'{"ATM Simulator" : ^40}')
print("  Your Current Balance Is:", locale.currency(deci_balance, grouping = True))
print("")
print(f'{"Deposit: D" : ^40}')
print(f'{"Withdraw: W" : ^40}')
print(f'{"Quit: Q" : ^40}')
print("****************************************")
#This code functions as the "main menu" and displays the current balance, 
#formats the balance using the currency module, groups it together,
#and tells the user the three letters they can use to navigate the simulated ATM

interface_input = input("Enter Your Selection: ")
transaction_input = 0.00
if interface_input == "D":
    transaction_input = float(input("Enter amount of transaction: "))
    print("****************************************")
    print("Your new balance is:", transaction_input + deci_balance)
    print("****************************************")
elif interface_input == "W":
    transaction_input = float(input("Enter amount of transaction: "))
    print("****************************************")
    print("Successfully withdrew", locale.currency(transaction_input, grouping = True))
    print("Your new balance is:", deci_balance - transaction_input)
    print("****************************************")
elif interface_input == "Q":
    print("Goodbye!")
else:
    print("****************************************")
    print(f'{"Invalid Selection" : ^40}')
    print("****************************************")
#This code runs after the main menu and has a logic statement for deposits, withdraws, quitting, 
#and invalid inputs. Deposit adds the numerical input with the original balance, 
#withdraw subtracts the numerical input from the original balance,
#quitting displays a farewell message, and anything else displays invalid selection

