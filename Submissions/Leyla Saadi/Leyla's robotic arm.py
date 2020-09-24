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

Arm_desired_distance = 4

Arm_Current_Distance = 6

if Arm_Current_Distance > 10:
    print('Move faster')
    print('Move 3 Forward')
elif (Arm_Current_Distance > 5) & (Arm_Current_Distance <= 10):
    print('Move at the same speed')
    print('Move 3 Forward')
elif 5 > Arm_Current_Distance > Arm_desired_distance:
    print('Reduce the speed')
    if Arm_Current_Distance < 3:
        move = (Arm_desired_distance - Arm_desired_distance) / 2
elif Arm_Current_Distance < Arm_desired_distance:
    print('STOP')



#If distance is bigger than 10 cm then move faster
#If distance is bigger than 5 cm then move at the same speed
#If distance is between the desired distance and 5cm then reduce the speed
#if distance is less than the desired one then stop