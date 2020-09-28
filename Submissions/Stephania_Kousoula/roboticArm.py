# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
# This script shows some conditionals and loops. It is about a robotic arm that moves around objects calculating
# distances.
##################################################
# Author: Stefania-Maria Kousoula
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: stefania-maria.kousoula@students.iaac.net
# Status: development
##################################################

# End of header section

desired_distance = 3 #the desired distance of the arm and the object, counted in cm, can be from 0 to 5
current_distance = 1 #the current distance between the arm and the object, counted in cm
formula = 0.5 * (current_distance - desired_distance)

if current_distance > 10:
    print("move faster")
if 5 <= current_distance <= 10:
    print("move at same speed")
if desired_distance < current_distance < 5:
    print("reduce speed")
elif current_distance < desired_distance:
    if current_distance < 3:
        print("move " + str(formula))
    else:
        print("STOP")
else:
    print ("move backwards")