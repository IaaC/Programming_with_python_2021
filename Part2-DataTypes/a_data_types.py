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



# declaring a value for a variable, in this case an Integer
print("my_data is")
my_data = 10
print(my_data, '\n')

print("it can change to another value like")
my_data = 10
print(my_data, '\n')

# using type() function, we can see the data type of a variable
print("it's data type is")
data_type = type(my_data)
print(data_type, '\n')

# we can also change the data type of a variable, in this case we change it to a Floating Point number
print("we can change it's data type")
my_data = 10.00
print(my_data)
data_type = type(my_data)
print(data_type)
print("we can also change it like this")
my_data = int(my_data)
data_type = type(my_data)
print(data_type, '\n')

print("you can use arithmetic operations + - * / ")
new_data = my_data + my_data
print(new_data)

blocks = 4
building_per_block = 60
num_buildings = blocks * building_per_block
print(num_buildings, '\n')

print("you can reassign them with reference to the same object")
my_data = my_data / my_data
print(my_data, '\n')

# String data types
print("another data type is String")
print("strings are defined by \" \" or \' \' ")
my_data = "This is a text"
print(my_data)
data_type = type(my_data)
print(data_type, '\n')

print("we can do string concatenation using + sign")
my_data = "hello" + " world"
print(my_data)
print("'1' + '0' = 10 ")
my_data = '1' + '0'
print(my_data, '\n')

print("and sting multiplication using * sign")
my_data = "a"
repeat = 10
new_data = my_data * repeat
print(my_data)
print(new_data, '\n')

# print ("we cannot mix data types in arithmetic operations")
# text_val = "10"
# num_val = 5
# sum = text_val + num_val
# print (sum)

print("Strings are 'ordered sequences' which means we can use indexing or slicing to separate a part of it")
my_data = "hello"
first_character = my_data[0]
second_character = my_data[1]
sub_data = my_data[0:2]
last_character = my_data[-1]
print(first_character)
print(second_character)
print(sub_data)
print(last_character)
print("hello has", len(my_data), "characters")