"""
Description: Interest update file for assignment 3
Author: Dante Daciuk
Date: 7/2/24
"""
import os
import pprint 
import csv 
niceprint = pprint.PrettyPrinter() 
balance_dictionary = { }

with open("account_balances.txt", "r") as input_file:
    for line in input_file:
        account_num, account_balance = line.strip().split('|')
        balance_dictionary[account_num] = float(account_balance)

niceprint.pprint(balance_dictionary)

for acc in balance_dictionary:
    current_balance = balance_dictionary[acc]
    if current_balance < 0:
        interest_rate = 0.1
    elif current_balance < 1000:
        interest_rate = 0.01
    elif current_balance < 5000:
        interest_rate = 0.025
    else:
        interest_rate = 0.05
    balance_dictionary[acc] = current_balance + ((current_balance * interest_rate) / 12)

print("Updated balances: ")
niceprint.pprint(balance_dictionary)