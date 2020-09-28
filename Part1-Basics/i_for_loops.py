# encoding: utf-8

##################################################
# This script shows an example of comparison operators.
# First, it shows examples of - for - loops.
# These loops serve to repeat operations for a defined number of times.
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

# We are using a basic for loop first

print('Lets print a series of numbers')


for i in range(10):
    print(i)

print('................................')
print('You can also use the counter vaule as part of internal functions')
text = 'This is iteration number: '
for i in range(11, 20, 3):
    print(text + str(i))
print('range(start_val, end_val, steps)')

print('................................')
print('You can also create some shapes: ')
text = '@'
character = '@'
for i in range(1, 10):
    text += character
    print(text)


print('................................')
print('Nested loops are quite useful. Here an example')
for i in range(1, 10):
    text = ''
    for j in range(0, i):
        text += str(i)

    print(text)


# Now combined with conditionals
reference_number = 3
text = ' can be divided into '
print('................................')
print('This are numbers which can be divided into ' + str(reference_number))
for i in range(1, 100):
    residual = i % reference_number
    # print('Residual value of dividing ' + str(i) + ' / ' + str(reference_number) + ' = ' + str(residual))
    if residual == 0:
        print(str(i) + text + str(reference_number))


# Try to print prime numbers smaller than 100
