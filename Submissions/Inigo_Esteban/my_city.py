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

print('The city where I live is {}'.format(city_name))
print('It´s population is {} and {}'.format(city_area, city_population) + ' and the city density is {}'.format(city_density))
print('and the city density is {}'.format(city_density))
