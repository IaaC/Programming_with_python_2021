# encoding: utf-8

##################################################
# This script shows an example of comparison operators.
# First, it shows examples of - while - loops.
# These loops serve to repeat operations until a condition is valid.
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

# We don't need any library so far

# We are using a simple condition to test

condition = 20
print('Check numbers lower than ' + str(condition))

i = 0
while i < condition:
    print('i = ' + str(i) + ' is lower than ' + str(condition))
    i += 1
else:
    print("i is no longer less than " + str(condition))
