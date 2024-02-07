"""
Description: Bank transactions file for assignment 3
Author: Dante Daciuk
Date: 7/2/24
"""
interface = {"D", "W", "Q"}
import random
random_balance = random.randint(-1000, 10000)
dec_random_balance = float(random_balance)
print("****************************************")
print(f'{"PIXELL RIVER FINANCIAL" : ^40}')
print(f'{"ATM SIMULATOR" : ^40}')
print("  Your current balance is: $", dec_random_balance)
print("")
print(f'{"Deposit: D" : ^40}')
print(f'{"Withdraw: W" : ^40}')
print(f'{"Quit: Q" : ^40}')
print("****************************************")