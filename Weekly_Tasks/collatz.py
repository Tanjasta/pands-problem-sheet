# collatz.py
# This program asks the user to input any positive integer and outputs the successive values of the following calculation
# At each step program calculates the next value 
# It taks the current value and, if it is even, divids it by two, but if it is odd, multiplies it by three and add one
# The program ends if the current value is one
# Author: Tatjana Staunton

number = int (input ("Please enter a positive integer: ")) # asks user to input any positive int
while number != 1: # if user puts 1, program stops if not one will print number
    print (int (number)) # int added to get number in format without .0
    if number % 2 == 0: # if number even then number = number devided by 2
        number = number / 2
        print (int (number)) # int added to get number whitout .0
    else:
        number = number * 3 + 1  # if numbrer not even, then * by 3 and add 1
        print (int (number)) # int added to get number in format with no .0

