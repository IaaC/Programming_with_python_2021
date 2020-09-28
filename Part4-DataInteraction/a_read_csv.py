# encoding: utf-8

##################################################
# This script shows an example of comparison operators.
# First, it shows how to read a CSV File.
# These files are very common data source when programming with python
# or performing analysis
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

# We will use the csv library
import csv


def get_gradient(max, min):
    if len(max) == len(min):
        grad = []
        for i in range(len(max)):
            gradient = max[i] - min[i]
            grad.append(gradient)
        return grad
    else:
        print('Gradient error, the lists given have different sizes')
        return []


# Let's define the lists in which we will store data
month = []
temp = []
temp_max = []
temp_min = []

with open('../Data/climatology_values_barcelona-fabra.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            month.append(row[0])
            temp.append(float(row[1]))
            temp_max.append(float(row[2]))
            temp_min.append(float(row[3]))
            line_count += 1
    print(f'Processed {line_count} lines.')

# We have data for 12 months plus the yearly average. So we start using only the first 12 values
month = month[0:12]
temp = temp[0:12]
temp_max = temp_max[0:12]
temp_min = temp_min[0:12]


temp_gradient = get_gradient(temp_max, temp_min)
temp_gradient_mean = sum(temp_gradient) / len(temp_gradient)
temp_max = max(temp_gradient)
print(temp_gradient)
print(temp_gradient_mean)

# get month with highest lowest or average.

#temp_gradient.index(temp_max)


# Then start with graphs





