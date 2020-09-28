# encoding: utf-8

##################################################
# This script how to read a CSV File.
# These files are very common data source when programming with python
# or documenting your work
#
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We will use the csv library
import numpy as np
import cv2

# Using cv2.imread() method
image = cv2.imread('../Data/photo.jpg')

# Displaying the image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destoryAllWindows()