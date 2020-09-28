# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: JEO
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: juan.eduardo.ojedea@students.iaac.net
# Status: development
##################################################

# End of header section


city_name = "Santiago de Chile"
city_area = 641
city_population = 5.6
city_density = city_population/city_area
print('...............................................\n')
print(city_name + ' is the capital of Chile \n')

area = str(city_area)
population = str(city_population)
density = str(city_density)

print('...............................................\n')
print("The population of "+ city_name + " is " + (population) + " million")
print("The area of " + city_name + " is " + (area) + " square kilometers")
print("The density of " + city_name +" is " + density)

