# accounts_extra.py
# This program reads in an account numbers of any length
# Outputs the account number of any lenghth with only 4 last digits displayed and the numbers before that replaced with X
# Author: Tatjana Staunton

account_number = input("Please enter your account number: ") # we are geting input from the user to enter their acount number
length = len(account_number) # Gets the length of the account number
if length < 10: # If the account number is shorter than 10 characters, print an error message and exit
    print("Invalid account number. Please enter a valid account number.")
    exit()
masked_account_number = "X" * 6 + account_number[6:length-4] + account_number[length-4:length]# Masks the first 6 digits with X and displays only the remaining digits
print (masked_account_number) # outputs account number with first 6 digits masked by X.
