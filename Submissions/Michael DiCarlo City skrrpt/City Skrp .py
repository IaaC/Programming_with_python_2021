
# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Michael R. DiCarlo
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Robotics and Advanced Constructrion group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Michael R. DiCarlo
# Email: MichaelrDiCarlo@gmail.com
# Status: developer
##################################################

# End of header section

city_Bagel = "Bagel index"
city_name = "Brooklyn"
city_bagels_p_block = 4000
city_population = 200000
city_blocks = 120
Bagel_index = city_bagels_p_block/city_blocks
People_per_Block = city_population/city_blocks
bagels_per_person = (city_population/city_blocks) / Bagel_index

print(city_Bagel)
print(city_name)
print("population total", city_population)
print("BK Bagel Per Block index", Bagel_index, "BPB")
print("People per Block", People_per_Block, "PBP" )
print("bagel to person ratio", bagels_per_person, "BPP")





