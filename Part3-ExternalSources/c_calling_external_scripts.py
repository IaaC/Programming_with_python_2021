# encoding: utf-8

##################################################
# This script shows an example of a script  calling an third-party script that serves to simplify programming.
# It uses the -- import -- command to refer to the external script.
# These ways of using or structuring source code are very common when programming with python
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

# We need to call the library we named -- ourlib --

import ourlib.our_script

ourlib.our_script.our_help()
