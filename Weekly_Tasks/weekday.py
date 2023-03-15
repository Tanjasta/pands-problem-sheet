# weekday.py
#This program outputs whether or not today is a weekday
# If today is a weekday it uotputs 'Yes, unfortinately today is a weekday.'
# If today is a weekend day it outputs 'It is a weekend, yay.'
# Author: Tatjana Staunton


import datetime # used import datetime to import datetime module
today = datetime.date.today () # Assigned value to today to get current date
if today.weekday () < 5: # used weekday () method 
# This method recognises day of the week as an int, where Mon is 0 and sun is 6, so week days will be the days that are less than 5
    print ("Yes, unfortinately today is a weekday.") # when day as int is less than 5 it prints 'Yes, unfortinately today is a weekday.'
else:
    print ("It is a weekend, yay.") # when day as int greater than 5 it prints out 'It is a weekend, yay.'