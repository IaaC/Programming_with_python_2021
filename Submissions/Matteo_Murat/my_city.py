# encoding: utf-8

##################################################
# Author: Matteo Murat
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Matteo Murat
# Email: matteo.murat@students.iaac.net
# Status: development
##################################################

# End of header section


city_name = 'Rome'
city_area = 12685
city_population = 2873000
city_density = city_population/city_area

print('Population Density')
print(city_density)

# or you can write it in this way
print('Population Density:'+ str(city_density) + ' inhabitants per km2')