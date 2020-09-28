##################################################
# This script was written to present informations about my hometown, Goiânia,
# as the first submission for the pre-course of Programming at IAAC, by professor Diego Pajarito.
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



city_name = 'Goiânia'
city_foundation_year = 1933
city_area = 728
city_population = 1536000
city_age = 2020-city_foundation_year
city_density = city_population//city_area

print('My city is called ' + str(city_name) + ' and it has ' + str(city_age) + ' years old.\n')
print('The population density in ' + str(city_name) + ' is ' +str(city_density) + ' inhabitants per km².')
