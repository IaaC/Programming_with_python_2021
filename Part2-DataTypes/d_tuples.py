# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Soroush Garivani
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Soroush Garivani
# Email: soroush.garivani@iaac.net
# Status: development
##################################################

# End of header section


# tuples
print("tuples are very similar to lists")
print("the are defined by ()")
my_tuple = (1, 2, 3)
print(my_tuple)
data_type = type(my_tuple)
print(data_type, '\n')

print("tuples can have different data types as items")
my_tuple = ('One', 'Two', 3)
print(my_tuple, '\n')

print("you can use indexing and slicing for tuples")
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:2], '\n')

# print ("the difference between tuples and lists is that tuples are 'immutable'. This means once they are assigned they cannot be reassigned.")
# my_list = [1,2,3,4]
# my_tuple = (1,2,3,4)
# my_list[0] = 'ONE'
# print (my_list)
# my_tuple[0] = 'ONE'
# print (my_tuple)
# # tuples are useful when you want to make sure your elements will not change during the program
