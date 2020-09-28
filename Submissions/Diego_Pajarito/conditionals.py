# encoding: utf-8

##################################################
# This script shows an example of a the use of conditionals during the class of
# September the 21 2020
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

# End of header section

my_city_name = 'Barcelona'
my_city_population = 5500000
my_previous_city_name = 'Bogota'
my_previous_city_population = 6500000

if my_city_population > 10000000:
    print('My City is a Megacity')
elif my_city_population > 1500000:
    print('My City is a large metropolitan area')
    if my_city_population > my_previous_city_population:
        print('My city is bigger than the previous')
    else:
        print('My previous city is bigger than the current one')
elif my_city_population > 500000:
    print('My City is a metropolitan area')
elif my_city_population > 200000:
    print('My City is a medium urban area')
else:
    print('My city is neither a Megacity nor a large metropolitan area')




