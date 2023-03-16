

def sqrt_approx(num): # define function with number (num) which used to find an approximation of its square root

    if num < 0: # If number less than 0 means that is negative number (sqrt cannot be counted from negative number),
        # the error ValueError prints out
        print ("ValueError")
    if num == 0: # If number equals to 0, it outputs 0
        return 0
    i = 1 # Start a var i and give value of 1
    while i*i <= num: # in while loop while the square of i is less than or equal to num
        i += 1 # Increments i by 1 until the square of i is greater than num
    return i-1 # then returns i-1, which is the integer square root of num


num = float(input("Enter a positive floating-point number: ")) # Asking for input from the user
approx = sqrt_approx(num) # Define value for approx
if approx is None: # If approx has no value, Error prints out
    print("Error: invalid input")
else:
    print(f"The square root of {num} is approximately {approx}") # Prints out square root approximation of the number entered by user
