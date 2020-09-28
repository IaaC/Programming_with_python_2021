# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Iñigo Esteban
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: inigo.esteban.marina@iaac.student.net
# Status: development
##################################################
##################################################

# Imagine robotic arm designed to locate itself at a given distance to an object.
# The following are the rules defined to control such arm and set the next action to take.
#
# First decision based on distance to an object
#
#     If distance is bigger than 10 cm then move faster
#     If distance is bigger than 5 cm then move at the same speed
#     If distance is between the desired distance and 5cm then reduce the speed
#     if distance is less than the desired one then stop
#
# Second decision based on direction
# By default the arm will move 3 cm forward but when the arm is located closer to 3cm to the object,
# the algorithm has to use a formula to calculate the distance to move. The arm will move half of the
# difference between the current location and the desired one. However, when the arm is closer to
# the object than the desired distance, the arm has to move backwards.
#
#
# Write a python script that, first, stores the desired distance to the object (between 0 and 5 cm)
# and the current distance and, second, prints out the action to follow together with the distance
# to move and the speed (faster/same/slower) based on the rules set.
# Test out your script by using multiple values for the variables and share your experience with the class.
##################################################

# First we define two variables in order to store the initial values:
desired_distance = 1
current_distance = 20
step = 0

# Now we define a while loop in order to define every situation and handle with it, printing the current state.
while current_distance != desired_distance:
    if current_distance > 10:
        print('The arm is moving faster')
        current_distance -= 3
        print('The current distance is ' + str(current_distance) + ' cm')
    elif current_distance > 5:
        print('The arm is moving at the same speed')
        current_distance -= 3
        print('The current distance is ' + str(current_distance) + ' cm')
    elif current_distance > desired_distance and current_distance < 5:
        if current_distance > 3:
            print('The arm is reducing the speed')
            current_distance -= 3
            print('The current distance is ' + str(current_distance) + ' cm')
        else:
            print('The arm is reducing the speed')
            current_distance = current_distance - (current_distance - desired_distance) / 2
            print('The current distance is ' + str(current_distance) + ' cm')
    else:
        print('The arm has stopped and is moving backwards')
        current_distance += 1





