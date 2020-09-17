# encoding: utf-8

##################################################
# This script shows an example of comparison operators.
# First, it shows different options for comparing values and operators.
# This operators serve to test when values are different or no.
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

# We don't need any library so far

# Let's write our code

print('These are few examples of comparison operators in python\n')

# We have already used addition: (+) and subtraction (-). Let's mix them with multiplication (*) and division (/)
numeric_value_1 = 10
numeric_value_2 = 20
numeric_value_3 = 15
numeric_value_4 = 10
text_value_a = 'sun'
text_value_b = 'moon'
text_value_c = 'mars'
text_value_d = 'sun'

print('Some examples of - equal (==) - and - not equal (!=) - operators:')
result = numeric_value_1 == numeric_value_2
print('Is numeric vale 1 equal to numeric value 2?')
print(result)
result = numeric_value_1 != numeric_value_2
print('Are they different?')
print(result)
result = numeric_value_1 == numeric_value_4
print('Is numeric vale 1 equal to numeric value 4?')
print(result)

print('............................')
print('Now examples with text variables')
result = text_value_a == text_value_b
print('Is text vale a equal to text value b?')
print(result)
result = text_value_a != text_value_b
print('Are they different?')
print(result)



# Lastly, operators dealing with diferences ( < | <= | > | >=)
result = numeric_value_4 < numeric_value_3
print('............................')
print('Some examples of - less than (< | <=) - and - greater than (> | >=) - operators:')
print('Is numeric value 4 lower than numeric value 3?:')
print(result)
result = numeric_value_4 <= numeric_value_1
print('Is numeric value 4 lower or equal to numeric value 1?:')
print(result)


result = text_value_a < text_value_b
print('............................')
print('These operators work with text values as well:')
print('Is text value a lower than text value b?:')
print(result)
result = text_value_a <= text_value_d
print('Is text value a lower or equal to text value b?:')
print(result)

