#
##################################################
# Author: Leyla Saadi
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Leyla Saadi
# Email: leyla.saadi@student.iaac.net
# Status: development
##################################################

# End of header section

Arm_desired_distance = 1

Arm_Distance = 3

if Arm_Distance > 10:
    print('Move faster')
if Arm_Distance > 5:
    print('Move at the same speed')
elif 5>Arm_Distance>0:
    print('Reduce the speed')
if Arm_Distance < Arm_desired_distance:
    print('STOP')



#If distance is bigger than 10 cm then move faster
#If distance is bigger than 5 cm then move at the same speed
#If distance is between the desired distance and 5cm then reduce the speed
#if distance is less than the desired one then stop