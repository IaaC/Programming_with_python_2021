##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# This is my first script in pyCharm.
##################################################
#
##################################################
# Author: Stephania-Maria Kousoula
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: stefania-maria.kousoula@students.iaac.net
# Status: development
##################################################

# End of header section

my_name = 'Stephania'
city_name = "Patras"
city_area = 125.4 #square meters
city_population = 167446 #people
city_density = city_population/city_area


print('Hello World!')
print('My name is ' + str(my_name) + '.')
print('My homecity is ' + str(city_name) + ' and is located in the west part of Greece.')
print('The population of ' + str(city_name) + ' is ' + str(city_population) + ' inhabitants.')
print('and the total area of the city is ' + str(city_area) + ' sq.m.')
print('The population density of ' + str(city_name) + ' is:')
print(city_density)