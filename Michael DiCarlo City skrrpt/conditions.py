# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Michael DiCarlo
# Email: MichaelrDiCarlo@gmail.com
# Status: development
##################################################

# End of header section


my_city = 'Brooklyn'
My_city_pop_in_mil = 2.5
My_city_pop = My_city_pop_in_mil * 1000000


#Megacity > 10000000
#Large_met_area > 1500000
#Met_area > 500000
#Medium_size_urban_area > 200000
#Small_size_urban_area > 50000


if My_city_pop > 10000000:
    print("my city is MEGA\n")
elif My_city_pop < 1.5*1000000:
    print('My city is large enough\n')
else:
    print('my city is still p big\n')
    print(My_city_pop)

#Megacity > 10000000
#Large_met_area > 1500000
#Met_area > 500000
#Medium_size_urban_area > 200000
#Small_size_urban_area > 50000
