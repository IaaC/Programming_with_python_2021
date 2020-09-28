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


# lists
print("use [] to declare lists")
my_list = []
print(my_list)
my_list = [1, 2, 7]
print(my_list)
data_type = type(my_list)
print(data_type, '\n')

print("it's possible to have different data types in a list")
my_list = [1, 0.10, 'a']
print(my_list, '\n')

print("use len() to count the items in a list")
len_list = len(my_list)
print(len_list, '\n')

print("indexing or slicing in a list")
first_item = my_list[0]
last_item = my_list[-1]
sub_list = my_list[0:2]
print(first_item)
print(type(first_item))
print(last_item)
print(type(last_item))
print(sub_list, '\n')


print("adding lists together")
list_a = [1, 2]
list_b = ['Three', 'Four', 'Five']
my_list = list_a + list_b
print(my_list, '\n')

print("change an item from the list")
my_list[3] = 4
print(my_list,'\n')

print("add an item to a list")
new_item = 'Six'
my_list.append(new_item)
print(my_list,'\n')
# note that append adds the item at the end of the list

print("use reverse() to reverse the order of items in a list")
my_list.reverse()
print(my_list)