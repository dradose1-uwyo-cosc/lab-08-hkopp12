# Hawkins Kopp
# UWYO COSC 1010
# Submission Date
# Lab 08
# Lab Section: 16
# Sources, people worked with, help given to:
# Class note, lab notes
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def in_or_float(string_to_check):
    try:
        # Try converting the string to float
        return_value = float(string_to_check)
        
        # Check if it's a float with one decimal point
        if string_to_check.count('.') == 1:
            return return_value
    except ValueError:
        pass

    return False

print (in_or_float)

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
 
def slope_intercept(m, b, a, an): #a=1 b=
    y_arr = []
    return y_arr

while True:
    m_input = input("Enter slope (m):")
    if m_input.lower() == 'exit':
        break

    b_input = input("Enter intercept (b):")
    if b_input.lower() == 'exit':
        break

    lower_x_input = input("Enter lower x bound:")
    if lower_x_input.lower() == 'exit':
        break

    upper_x_input = input("Enter upper x bound:")
    if upper_x_input.lower() == 'exit':
        break


print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
# Use code from part 1

import math

def in_or_float(string_to_check):
    try:
        return_value = float(string_to_check)

        if string_to_check.count('.') == 1:
            return return_value
    except ValueError:
        pass

def Quadratic_formula(a, b, c):

    a = in_or_float(a)
    b = in_or_float(b)
    c = in_or_float(c)

    if a is False or b is False or c is False:
        return "Invalid input: coefficients must be integers or floats."

    if a == 0:
        return "Coefficient 'a' cannot be zero in a quadratic equation."

