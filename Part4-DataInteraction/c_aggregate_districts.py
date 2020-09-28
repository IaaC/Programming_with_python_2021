# encoding: utf-8

##################################################
# This script interacts with data files to extract information and modify values given to a function.
# It is part of an exercise in which data about districts and neighbourhoods are processed
# Here we have the second part of the script that calls an external script to read neighbourhoods data
#
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# Here we refer to the third-party scripts
import disctlib.district as d
import disctlib.neighbour as n


# Here some global variables to set paths and other details
districts_path = '../Data/districts_BCN.csv'
neighbourhoods_path = '../Data/neighbourhoods_BCN.csv'


# These two lines serve to read data from files
n.read_neighbourhoods(neighbourhoods_path)
d.read_districts(districts_path)


# We now will see the way to aggregate data at the district level
# we save district and neighbourhood data into local variables
my_districts = d.get_districts()
my_neighbourhoods = n.get_neighbourhoods()
# print(my_neighbourhoods)

# We use a for loop to go through districts list
for single_district in my_districts:
    # This line prints each district name located at position two of each internal list
    print(single_district[2])
    # This line gets the district code and saves it into a variable
    d_code = single_district[0]
    # We need to set a variable for population. It starts from 0 for every districtc
    population = 0
    ############
    # This embedded for serves to go through the neighbourhoods. Be aware of the key values of this dict
    for dict_item in my_neighbourhoods:
        # We get the key value for each neighbourhood. There are pairs of keys and individual dicts.
        n_dict = my_neighbourhoods[dict_item]
        # We need to compare district and neighbourhood codes and only when they match we proceed
        if n_dict['COD_DISTRICT'] == d_code:
            # Here we add neighbourhood population to the district population variable
            population += n_dict['POPULATION']
    # Once the internal loop has finished, we can print the total and proceed with calculating density
    print(population)
    density = population / single_district[1]
    print('Density: ', round(density,1), ' hab/Km2')

