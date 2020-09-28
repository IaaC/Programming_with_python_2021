##################################################
# This script was written to present informations and conditionals about my hometown, Goiânia,
# as the second submission for the pre-course of Programming at IAAC, by professor Diego Pajarito.
##################################################
#
##################################################
# Author: Laura Guimarães
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# Maintainer: Laura Guimarães
# Email: laura.figueiredo@students.iaac.net
# Status: development
##################################################

# End of header section


my_city_name = 'Goiânia'
my_city_population = 1536000
my_current_city_name = 'Barcelona'
my_current_city_population = 5500000

if my_city_population > 10000000:
    print('My city is a megacity.')
elif my_city_population > 1500000:
    print('My city is a large metropolitan area.')
    if my_city_population > my_current_city_population:
        print('My city is bigger than my current city.')
    else:
        print('My current city is bigger than my city.')
elif my_city_population > 500000:
    print('My city is a metropolitan area.')
elif my_city_population > 200000:
    print('My city is a medium size urban area.')
elif my_city_population > 50000:
    print('My city is a small urban area.')
else:
    print ('My city is a small city.')

