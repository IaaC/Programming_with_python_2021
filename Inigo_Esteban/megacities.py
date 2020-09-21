# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Iñigo Esteban
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: inigo.esteban.marina@iaac.student.net
# Status: development
##################################################

city_name = 'Madrid'
city_area = 604.5 # the units are in km²
city_population = 6.642 # the units are in millions
city_density = round(float(city_population / city_area), 3) # the units are in millions/km²

megacity_01 = 'New York'
megacity_01_population = 8.5
megacity_02 = 'London'
megacity_02_population = 8.42
megacity_03 = 'Beijin'
megacity_03_population = 21.54

# print('The city where I live is {}'.format(city_name))
# print('It´s population is {} and {}'.format(city_area, city_population) + ' and the city density is {}'.format(city_density))
# print('and the city density is {}'.format(city_density))

city = megacity_02
city_pop = megacity_02_population
megacity_list = []
large_metropolitan_area_list = []
metropolitan_area_list = []
medium_size_urban_area_list = []
small_urban_area_list = []
big_list = [megacity_list, large_metropolitan_area_list, metropolitan_area_list,
            medium_size_urban_area_list, small_urban_area_list]


if city_pop > 10:
    print('My city is a Megacity')
    megacity_list.append(city)
elif city_pop > 1.5:
    print('My city is a large metropolitan area')
    large_metropolitan_area_list.append(city)
elif city_pop > 0.5:
    print('My city is a metropolitan area')
    metropolitan_area_list.append(city)
elif city_pop > 0.2:
    print('My city is a medium size urban area')
    medium_size_urban_area_list.append(city)
else:
    print('My city is a small urban area')
    small_urban_area_list.append(city)

print(big_list)

print('End of Script')

##################################################
# categories:
# megacity > 10
# large metropolitan area > 1.5
# metropolitan area > 0.5
# medium size urban area > 0.2
# small urban area > 0.05