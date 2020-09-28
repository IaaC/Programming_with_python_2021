# encoding: utf-8

##################################################
# This script shows an example of arithmetic operators.
# First, it shows different options for using arithmetic operators.
# This operators allow to perform basic arithmetic calculus.
#
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We don't need any library so far

# Let's write our code

print('These are few examples of arithmetic operators in python\n')

# We have already used addition: (+) and subtraction (-). Let's mix them with multiplication (*) and division (/)
result = 1 * 2 + 6 / 3
print('The result of calculating - 1*2 + 6/3 - is:')
print(result)
print('Do not forget the concept of precedence within arithmetic operators. '
      'There are differences when using operators in different positions')
result = 1 + 2 - 3 * 4 / 5
print('The result of - 1 + 2 - 3 * 4 / 5 - is: ')
print(result)
result = 1 / 2 * 3 - 4 + 5
print('Is different than the result of - 1 / 2 * 3 - 4 + 5 -: ')
print(result)


# Lastly, there are additional arithmetic functions
result = 20 % 8
print('............................')
print('If you want to know the reminder value when dividing two numbers you should use the modulus operator - % -')
print('The modulus result of - 20 % 8- is:')
print(result)


result = 20 // 8
print('............................')
print('If you want to know the quotient value when dividing two numbers you should use the modulus operator - // -')
print('The modulus result of - 10 // 4- is:')
print(result)

# See what happens when you divide negative numbers


result = 2 ** 8
print('............................')
print('If you want perform the power operation you should use the exponent operator - ** -')
print('The modulus result of - 2 ** 8 - is:')
print(result)
