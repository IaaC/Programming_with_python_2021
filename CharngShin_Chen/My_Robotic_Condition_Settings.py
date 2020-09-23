
####################################################################################################
# Author: CharngShin Chen
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: charngshin.chen@students.iaac.net
# Status: development
####################################################################################################



print('20200922_practice 01')
"""
# First decision based on distance to an object
# If distance is bigger than 10 cm then move faster
# If distance is bigger than 5 cm then move at the same speed
# If distance is between the desired distance and 5cm then reduce the speed
# if distance is less than the desired one then stop
"""
#units=cm
target_distance=2
desired_distance=3




# Condition 1
if 0<desired_distance<5:
    if target_distance > 10:
        print('The robotic arm will more faster')
    elif target_distance > 5:
        print('The robotic arm will move at the same speed')
    elif desired_distance < target_distance < 5:
        print('The robotic arm will reduce the speed')
    elif target_distance < desired_distance:
        print('The robotic arm will stop')

# Condition 2
if 0 < desired_distance < 5:
    if target_distance < desired_distance:
        print('The robotic will run backwards')
    if target_distance < 3:
       distance = (target_distance - desired_distance)/2
       print('The robotic will run'+" "+str(distance)+'cm' )