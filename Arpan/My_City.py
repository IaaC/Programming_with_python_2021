# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author:Arpan Mathe
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Arpan Mathe
# Email: arpan.mathe@students.iaac.net
# Status: development
##################################################

# End of header section


<<<<<<< HEAD

=======
>>>>>>> 60fd01b21c132d6f0f95d728461ae514f29e7280
My_city_name = "Debrecen"
My_city_population = 250000
My_city_area = 460
My_city_young_population = 125000
My_city_elder_population = 75000
My_city_older_population = 50000

Population_density = My_city_population / My_city_area
Population_density_young = My_city_young_population / My_city_area
Population_density_elder = My_city_elder_population / My_city_area
Population_density_older = My_city_older_population / My_city_area

print("My City Name is =", My_city_name)
print("My City Population density =", int(Population_density))
print("Population density of young =", int(Population_density_young))
print("Population density of elder =", int(Population_density_elder))
print("Population density of older =", int(Population_density_older))

age = int(input("enter you age"))

if age <= 18:
    print("You are young and counted under young population")
elif age > 18 > 60:
    print("You are elder and counted under elder population")
else:
    print("You are old and counted under old population")
<<<<<<< HEAD

=======
    
>>>>>>> 60fd01b21c132d6f0f95d728461ae514f29e7280
