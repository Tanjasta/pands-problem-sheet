# pythonbank.py
# This program prompts the user to enter two amouns and reads in two money amounts (in cent)
# Adds the two amounts together
# Prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Tatjana Staunton
# Enter amount1(in cent): 65
# Enter amount2(in cent): 180
# The sum of these is €2.45
# 

x = int (input ("Enter amount1 (in cent):")) # we get an input of 65 from the user
y = int (input ("Enter amount2 (in cent):")) # we get an input of 180 from the user
answer = int (x + y) # we get sum of two amounts 
answer = int ( x + y)/100 # added /100 to get amount in format of euro and cent ( because 100 cent in one euro)
print (" {} plus {} The sum of this is € {}" .format (x, y, answer)) 
#prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent 
