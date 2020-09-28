# encoding: utf-8

##################################################
# This script interacts with data files to extract information and modify values given to a function.
# It is part of an exercise in which data about districts and neighbourhoods are processed
# Here we have the firs part of the script that calls an external script that reads districts data
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


# Here some global variables to set paths and other details

districts_path = '../Data/districts_BCN.csv'

d.read_districts(districts_path)

print('Here you have a list of lists with the districts of Barcelona\n')
print(d.get_districts())




