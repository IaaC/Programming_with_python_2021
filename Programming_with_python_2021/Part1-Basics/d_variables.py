# encoding: utf-8

##################################################
# This script shows an example of variable assignment. It explores the different options for storing vales into
# variables
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

# Let's create two variables and assign them two values
i_am_a_variable = 1
i_am_another_variable = 2

# Let's assign the result of an operation to a third variable
i_store_the_result = i_am_a_variable * i_am_another_variable

# Let's print out the result
print('The value assigned is:')
print(i_store_the_result)
print('....................\n')

# Let's assign a new value to this variable and print again
i_store_the_result = i_am_a_variable - i_am_another_variable
print('The value assigned now is:')
print(i_store_the_result)
print('....................\n')

# We can also assign values or variable's values
i_am_a_variable = i_store_the_result
i_am_another_variable = 'Now I store text'

# Let's see how we ended up storing values
print('The value in -i_am_a_variable- now is:')
print(i_am_a_variable)
print('The value in -i_am_another_variable- now is:')
print(i_am_another_variable)
print('The value in -i_am_a_variable- now is:')
print(i_store_the_result)
print('....................\n')
