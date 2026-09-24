#Experiment 7:
#  Exception handling is a mechanism used to handle errors that occur during 
# program execution without stopping the entire program.
# Python mainly uses try and except blocks to handle exceptions.
# example 1:
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")
# The code inside try is executed first.
# Since dividing a number by zero causes a ZeroDivisionError, 
# the except block handles the error and displays a message instead of stopping the program

# example 2:
try:
    a = int(input("Enter a number: "))
    print("Number is:", a)

except ValueError:
    print("Please enter a valid number")
#  The try block attempts to convert the input into an integer.
# If the user enters something that is not a number, a ValueError occurs
# and the except block handles it