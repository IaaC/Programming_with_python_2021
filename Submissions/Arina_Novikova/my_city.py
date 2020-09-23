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

city_name = 'Moscow'
city_area = 2561
city_population = 12692466
city_density = city_population/city_area

print('The city I want to describe is {}'.format(city_name))
print(str('City Area =')+" "+str(city_area)+" "+'km²')
print(str('City Population =')+" "+str(city_population)+" "+'millions people')
print(str('Population Density =')+" "+str(city_density)+" "+'inhabitants per km²')
print('....................')