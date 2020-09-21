
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

# Calculation of the density of the city
city_name = "Naples"
city_area = 1130
city_population = 4250000
city_density = city_population/city_area
city_density2 = str(round(city_density, 2))

print("The population in"), print(city_name),print("is"),
print(city_density2)

# Calculation of the age of the city
city_year_foundation = -475
current_year = 2020
print("The city of Naples has")
print(current_year-city_year_foundation)
print("years")

# Name of the Mayor and days he is in charge
from datetime import date
name_mayor = "Luigi de Magistris"
day_first_election = date(2011, 6, 1)
current_day = date(2020, 9, 21)
years_power = current_day - day_first_election
print("The mayor is being in power for")
print(years_power.days)
print("days")



