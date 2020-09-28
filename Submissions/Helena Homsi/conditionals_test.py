# encoding: utf-8

##################################################
# This script shows an example of variable assignment. It explores the different options for storing vales into
# variables
##################################################
#
##################################################
# Author: Helena Homsi
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# Master:  Master in Robotics and Advanced Construction
# Email: helena.homsi@students.iaac.net
# Status: Student
##################################################

# We don't need any library so far

# Let's write our code

#FOR BEIRUT
my_city_name = 'Beirut'
my_city_population = 361000

#FOR DUBAI
my_old_city_name = 'Dubai'
my_old_city_population = 3331000

if my_city_population > 10000000:
    print(my_city_name + ' is a Megacity')
elif my_city_population > 1500000:
    print(my_city_name + ' is a Large Metropolitan City')
    if my_old_city_population > 1500000:
        print (my_old_city_name + ' is bigger than' + my_city_name)
    else:
        print (my_city_name + 'is bigger than' + my_old_city_name)
elif my_city_population > 500000:
    print(my_city_name + ' is a Metropolitan City')
elif my_city_population > 200000:
    print(my_city_name + ' is a Medium Size Urban City')
elif my_city_population > 50000:
    print(my_city_name + ' is a Small Size Urban City')


print ('\n')


