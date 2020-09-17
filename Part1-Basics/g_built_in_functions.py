# encoding: utf-8

##################################################
# This script shows an example of comparison operators.
# First, it shows different options to create functions used to simplify your code.
# These functions are used as other functions embedded in python.
#
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We are going to use random library
import random

# Let's write our code
print('You can use the - + - operator to concatenate text')
text = 'text fragment - '
result = text + text + text + '\n'
print(text + result)

print('These are few examples of python functions\n')
# For instance the - random integer - function from - random - library
number = random.randint(0, 10)
# Or the - print - function
print('Yes!! print is built-in function to print characters in the screen')
# Also functions for transforming variable type. Here the function - str -
print('Although this is a number can be printed as character: ' + str(number))


# There are also functions for building complex data structures
print('You can use the - range(n) - function to create a list with n numbers')
text = 'range(5) = '
result = range(5)
print(text + str(result))

print('You can use the - sum() - function to add up numbers')
text = '3 + 9 = '
result = sum(result)
print(text + str(result))

