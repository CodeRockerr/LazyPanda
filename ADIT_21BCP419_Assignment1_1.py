'''PROBLEM: WAP to take 2 float values to add, subtract, multiply and divide them and print their fractional representation.'''

# Importing the Fraction Module
from fractions import Fraction

# Enter the first float value
print("Enter first number :")
n1 = input()

# Enter the second float value
print("Enter second number :")
n2 = input()

# The below will give addition of two numbers
print("Addition is", float(n1) + float(n2))

# The below will give subtraction of two numbers
print("Subtraction is", float(n1) - float(n2))

# The below will give multiplication of two numbers
print("Multiplication is", float(n1) * float(n2))

# The below will give division of two numbers
print("Division is", float(n1) / float(n2))

# The below will give fractional representation of two numbers we entered
print(Fraction(n1) / Fraction(n2))

# Let's take first value as "5.3" and second value as "3.6"