# encoding: utf-8

##################################################
# This script interacts with data files to extract information and modify values given to a function.
# It is part of an exercise in which data about districts and neighbourhoods are processed
# Here we have the functions for manipulating information about neighbourhoods
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

# need libraries to read external files
import csv

neighbourhoods = dict()
tags = []


def read_neighbourhoods(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                tags =  row
                print(f'Column names are {", ".join(tags)}')
                line_count += 1
            else:
                neighbourhood = dict()
                neighbourhood[tags[0]] = int(row[0])
                neighbourhood[tags[2]] = row[2]
                neighbourhood[tags[3]] = int(row[3])
                neighbourhoods[row[1]] = neighbourhood
                line_count += 1
        print(f'Processed {line_count} lines.')


def get_neighbourhoods():
    return neighbourhoods
