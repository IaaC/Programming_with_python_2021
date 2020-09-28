# encoding: utf-8

##################################################
# This script interacts with data files to extract information and modify values given to a function.
# It is part of an exercise in which data about districts and neighbourhoods are processed
# Here we have the functions for manipulating information about districts
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

districts = []


def read_districts(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                district = []
                district.append(int(row[0]))
                district.append(float(row[1]))
                district.append(row[2])
                districts.append(district)
                line_count += 1
        print(f'Processed {line_count} lines.')


def get_districts():
    return districts


def get_district_name(code):
    name = 'Not found'
    for i in districts:
        if i[0] == code:
            name = i[2]
    return name


def add_population(code, population):
    print('your code will be here')
