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

my_city_name = "debrecen"
my_city_population = int(input("Please enter the population of your city"))
My_previous_city_name = "Dubai"
My_previous_city_population = int(input("Please enter the population of your previous city"))

if my_city_population > 10000000:
    print("your city is a Megacity")
    if my_city_population>10000000:
        print("your city is a Megacity")
    else:
        print("dubai is not a megacity ")
elif my_city_population > 1500000:
    print("Your city is a Large Metropolitan City")
    if my_city_population > 1500000:
        print("your city is a Megacity")
    else:
        print("dubai is not a megacity ")
elif my_city_population > 500000:
    print("Dubai is a Metro city")
    if my_city_population > 500000:
        print("Dubai is a Megacity")
    else:
        print("Dubai is not a Megacity ")
else:
    print("Your city is not a Megacity")
    if my_city_population < 500000:
        print("Dubai is a Megacity")
    else:
        print("dubai is not a Megacity ")