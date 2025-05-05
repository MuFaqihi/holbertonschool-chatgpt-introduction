#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a number n recursively.
# A factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# Factorial of n is defined as n! = n * (n-1) * (n-2) * ... * 1, and by definition, 0! = 1.

# Parameters:
# n (int): The number for which the factorial is calculated. It is expected to be a non-negative integer.
# Returns:
# int: The factorial of the number n. Returns 1 if n is 0 (base case of the recursion).

def factorial(n):
    if n == 0:  # Base case: if n is 0, return 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Main code to get the input from the command line
f = factorial(int(sys.argv[1]))  # Convert the first command-line argument to an integer and compute its factorial
print(f)  # Print the calculated factorial
