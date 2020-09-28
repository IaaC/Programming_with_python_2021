#############################################################
# Author: Diana Roussi
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia- IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diana Roussi
# Email: konstantina.roussi@students.iaac.net
# Status: architect
##############################################################
country_name = 'Greece '
city_name = 'Athens '
city_area = 361
city_population = 2664776
region = "Attica "
region_area = 3808
region_population = 3761810
def density(x, y):
 dens = x / y
 return dens
print()
print("Hello, I am from " + city_name + ", " + country_name)
print(city_name + "is the capital of " + country_name + " and belongs to the region of " + region)
print()
print(region + "is a peninsula and has a total area of ", region_area, ' km²')
print(region + " is very dense area with a density of around %d people per km²" % (density(region_population, region_area)))
print()
print(city_name + 'is one of the oldest cities in the world')
print(city_name + "has a total polulation of", city_population, "people")
print(city_name + "has a density of %d people per km²" % (density(city_population, city_area)))