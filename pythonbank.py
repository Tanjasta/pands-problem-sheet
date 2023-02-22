# $ python bank.py
# This program prompt the user and read in two money amounts (in cent)
# Adds the two amounts
# Prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Tatjana Staunton
# Enter amount1(in cent): 65
# Enter amount2(in cent): 180
# The sum of these is €2.45
# 

x = int (input ("Enter amount1 (in cent):")) # we get an input of 65 from the user
y = int (input ("Enter amount2 (in cent):")) # we get an input of 180 from the user
answer = int (x + y) # we get sum of two amounts
print (" {} plus {} The sum of this is € {}" .format (x, y, answer))