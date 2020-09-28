##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: CharngShin Chen
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: charngshin.chen@students.iaac.net
# Status: development
##################################################


my_city_name='Taichung'
my_city_population=2816792
london_city_population=10000000

if my_city_population > 100000:
    print('My city is a Metacity')

print('....................\n')
if my_city_population < london_city_population:
    print('My city is smaller than London')

print('....................\n')

if my_city_population > 100000:
    print('My city is a Metacity')
else:
    print('My city is Not a Metacity')

print('....................\n')

if my_city_population > 100000:
    print('My city is a Metacity')
elif my_city_population > 10000000:
    print('My city is a super Metacity')
else:
    print('My city is Not a Metacity neither suprt Metacity')

print('....................\n')

my_city_name='Taichung'
my_city_population=2816792
my_living_city_name='Barcelona'
my_living_city_population=5500000

if my_city_population > 10000000000:
    print('My city is a Metacity')
elif my_city_population > 100000:
    print('My city is a super Metacity')
    if my_city_population < my_living_city_population:
        print('My city is bigger than the living')
    else:
        print('My city is smaller than the living')
else:
    print('My city is Not a Metacity neither super Metacity')







