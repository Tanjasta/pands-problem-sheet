# $pythonaccounts.py
# This program reads in a 10 character account number
# Outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
# Author: Tatjana Staunton

# Please enter an 10 digit account number: 1234567890
# XXXXXX7890

account_number = input ("Please enter an 10 digit account number:") # we are geting input from the user to enter their acount number
'''print (account_number) # prints the number entered by the user
print (account_number [-4:]) # prints four last numbers'''
# line 13 is a new var with value where ((6 Xs that replased first 6 nr) + (the last for digits of the account number))
# in first braket, we take X and * it by 6 to get 6Xs and then add the second bracet where we get last 4 digits of the account nr
x_replaced_number = (("X" * 6) + (account_number [-4:]))  
print (x_replaced_number) # prints out the number that user put in in the format where the first 6 numbers are replased by Xs