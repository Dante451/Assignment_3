"""
Description: Interest update file for assignment 3
Author: Dante Daciuk
Date: 7/2/24
"""
import pprint 
import csv 
niceprint = pprint.PrettyPrinter() 
balance_dictionary = { }
#This parts imports several modules, and creates an empty dictionary 
#to place data inside
with open("account_balances.txt", "r") as input_file:
    for line in input_file:
        account_num, account_balance = line.strip().split('|')
        balance_dictionary[account_num] = float(account_balance)
#This part opens up the account_balances text file and places it into the dictionary,
#formatting and storing it
niceprint.pprint(balance_dictionary)
#This actually prints off said dictionary
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
#This part is an if/else statement that adds an interest rate based on the initial amount
print("Updated balances: ")
niceprint.pprint(balance_dictionary)
#This prints off the dictionary again but updated with the interest formula
with open("updated_balances_DD.csv", "w", newline="") as csvfile:
    fieldnames = ["Account", "Balance"]
    write = csv.DictWriter(csvfile, fieldnames = fieldnames)
    write.writeheader()
    for account, balance in balance_dictionary.items():
        write.writerow({"Account": account, "Balance": balance})
#This block of code creates a csv file, opens in write mode,
#writes into it, and updates the dictionary again
with open("updated_balances_DD.csv", "r") as myfile:
    reader = csv.DictReader(myfile)
    for row in reader:
        print(row)
#This part prints off the csv file content that is now updated once again,
#opened in read mode