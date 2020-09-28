# encoding: utf-8

##################################################
# This script shows an example of an external script that serves to simplify programming.
# First, it has a single functions that prints out a help text.
# These files are very common data sources when programming with python
# they serve to make code simpler and distribute individual parts of programs
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

# We do not need external libraries

text = 'This is the help text. It is printed by an external library which simplifies the way you' \
       'write code. This scirpt is inside a folder that has a python file -- __init__.py -- that ' \
       'indicates this is a python library and allows other scripts to call it using the ' \
       '-- import -- command'

print('our script was imported\n')


def our_help():
    print(text)

