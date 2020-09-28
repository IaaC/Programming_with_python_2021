##################################################
# Author: Alberto Browne
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Alberto Browne
# Email: alberto.eugenio.browne@students.iaac.net
# Status: development
##################################################

my_city_name = 'Panquehue'
my_city_population = 7273
my_actual_city_name = 'Barcelona'
my_actual_city_population = 5500000
my_oldest_city_name = 'Santiago'
my_oldest_city_population = 7112808

if my_city_population > 10000000:
    print('My City is a MegaCity')
elif my_city_population > 1500000:
    print('My city is a Large metropolitan area')
elif my_city_population > 500000:
    print('My city is a metropolitan area')
elif my_city_population > 200000:
    print('My city is medium urban area')
elif my_city_population > 50000:
    print('My city is a small urban area')
else:
    print('I live in a small town \n')

if (my_city_population > my_actual_city_population) & (my_city_population > my_oldest_city_population):
    result = my_city_name + 'is bigger than ' + my_actual_city_name + 'and ' + my_oldest_city_name
elif (my_actual_city_population > my_city_population) & (my_actual_city_population > my_oldest_city_population):
    result = my_actual_city_name + 'is bigger than ' + my_city_name + 'and ' + my_oldest_city_name
else:
    result = 'My city, ' +my_city_name + ', is smaller than ' + my_actual_city_name + ' and ' + my_oldest_city_name
    print(result)
    print('............. \n')
    print('end of script')
