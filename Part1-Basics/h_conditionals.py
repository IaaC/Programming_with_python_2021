# encoding: utf-8

##################################################
# This script shows an example of comparison operators.
# First, it shows examples of conditional operators.
# This operators serve to test when a condition happens or not.
#
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We don't need any library so far

# We are going to use some data about three European cities
# Data is approximate and comes from Wikipedia

print('These are few examples of comparison operators in python\n')

# We have already used addition: (+) and subtraction (-). Let's mix them with multiplication (*) and division (/)
city_1_name = 'Barcelona'
city_1_population = 5474482
city_1_unemployment_rate = 17.24
city_2_name = 'Lisbon'
city_2_population = 2827514
city_2_unemployment_rate = 7.4
city_3_name = 'Amsterdam'
city_3_population = 2431000
city_3_unemployment_rate = 3.3

# note: Mind the indented structure of if clauses. It matters!!!!

# - if - clauses serve for testing conditions to trigger actions if it is true
if city_1_population > city_2_population:
    result = city_1_name + ' is bigger than ' + city_2_name
    print(result)

# - if else - clauses serve for testing conditions and trigger an action whether if it is true or not
print('.......................')
if city_2_unemployment_rate > city_3_unemployment_rate:
    result = city_2_name + ' has a higher unemployment rate than ' + city_3_name
else:
    result = city_3_name + ' has a higher unemployment rate than ' + city_2_name
print(result)


# - if elif - clauses serve for adding more comparisons to an if clause
if city_1_unemployment_rate == city_3_unemployment_rate:
    result = city_1_name + ' has the same unemployment rate than ' + city_3_name
elif city_1_unemployment_rate < city_3_unemployment_rate:
    result = city_1_name + ' has a lower unemployment rate than ' + city_3_name
else:
    result = city_1_name + ' has a higher unemployment rate than ' + city_3_name
print(result)


# if and if elif clauses can use multiple conditions using logical operators AND / OR
if (city_1_population > city_2_population) & (city_1_population > city_3_population):
    result = city_1_name + ' is bigger than ' + city_2_name + ' and ' + city_3_name
elif (city_2_population > city_1_population) & (city_2_population > city_3_population):
    result = city_2_name + ' is bigger than ' + city_1_name + ' and ' + city_3_name
elif (city_3_population > city_1_population) & (city_3_population > city_2_population):
    result = city_3_name + ' is bigger than ' + city_1_name + ' and ' + city_2_name
else:
    result = 'We could not identify which city is bigger'
print(result)


# if, if elif and if else classes can be nested. Indentation plays the main role here
if city_1_population > city_2_population:
    if city_1_unemployment_rate > city_2_unemployment_rate:
        result = city_1_name + ' is bigger and has a higher unemployment rate than ' + city_2_name
    else:
        result = city_1_name + ' is bigger but has a lower unemployment rate than ' + city_2_name
else:
    if city_1_unemployment_rate > city_2_unemployment_rate:
        result = city_2_name + ' is bigger and has a higher unemployment rate than ' + city_1_name
    else:
        result = city_2_name + ' is bigger but has a lower unemployment rate than ' + city_1_name
print(result)
