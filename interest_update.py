"""
Description: Interest update file for assignment 3
Author: Dante Daciuk
Date: 7/2/24
"""
import os
import pprint 
pretty = pprint.PrettyPrinter()
balance_dictionary = { }
with open("account_balances.txt", "r") as input_file:
    for line in input_file:
        key, value = line.strip().split('|')
        balance_dictionary[key] = float(value)
pretty.pprint(balance_dictionary)
#Text to confirm repositories are connected