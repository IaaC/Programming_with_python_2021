# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Arina Novikova
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Arina Novikova
# Email: arina.novikova@students.iaac.net
# Status: development
##################################################

# End of header section

print('....................')

my_city_name = "Moscow"
my_city_population = 12692466
print('My city is {}'.format(my_city_name))

my_previous_city = "Belgorod"
my_previous_city_population = 394142
print('My previous city is {}'.format(my_previous_city))

if my_city_population > 10000000:
    print('My city is a Megacity')
elif my_city_population > 1500000:
    print('My city is a large metropolitan area')
elif my_city_population > 200000:
    print('My city is a medium size urban area')
elif my_city_population > 50000:
    print('My city is a medium size urban area')
elif my_city_population > 500000:
    print('My city is a metropolitan area')
if my_city_population > my_previous_city_population:
    print('My city is bigger than my previous city')
else:
    print('My previous city is bigger than my city')

print('....................')







