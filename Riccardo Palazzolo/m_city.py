
##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Riccardo Palazzolo Henkes
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Riccardo Palazzolo Henkes
# Email: riccardo.palazzolo@students.iaac.net
# Status: development
##################################################

# End of header section

city_name = "Naples"
city_area = 1130
city_population = 4250000
city_density = city_population/city_area
city_density2 = str(round(city_density, 2))

print("The population in"), print(city_name)
print(city_density2)

