# encoding: utf-8

##################################################
# This script shows an example of variable assignment. It explores the different options for storing vales into
# variables
##################################################
#
##################################################
# Author: Helena Homsi
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# Master:  Master in Robotics and Advanced Construction
# Email: helena.homsi@students.iaac.net
# Status: Student
##################################################

# We don't need any library so far

# Let's write our code

# All units are in cm

distance_of_object = 4
distance1 = 10
distance2 = 5
desired_distance = 3
distance_to_object = 2

# TASK 01
print('TASK 01: Speed of robot arm')
if distance_of_object > distance1:
    print('Arm must move faster')
elif distance_of_object > distance2:
    print('Arm must move at same speed')
elif distance_of_object in range(desired_distance,distance2):
    print('Arm must slow down speed')
elif distance_of_object < desired_distance:
    print('Stop activity')

print("\n")

# TASK 02
print('TASK 02: Distance to move')
if distance_to_object == desired_distance:
    print('Operate usually: move 3 cm closer')
elif distance_to_object < desired_distance:
    print('Arm must move ' + str((distance_to_object-desired_distance)/2) + ' cm')
elif distance_to_object > desired_distance:
    print('Arm must move backwards')

