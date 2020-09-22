#############################################################
# Author: Diana Roussi
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia- IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diana Roussi
# Email: konstantina.roussi@students.iaac.net
# Status: programming
##############################################################

current_distance = 2  # in cm
desired_distance = 4  # in cm
direction = "forward"
distance = 3  # in cm
action = "Move"

if 0<desired_distance <5 :

    if current_distance > 10:
        action = "move faster "
    elif current_distance > 5:
        action = "move at the same speed "
    elif current_distance > desired_distance:
        action = "reduce the speed and move "
    else:
        action = "stop and move "

    if current_distance < desired_distance:
        direction = "backward"
    elif current_distance < 3:
        distance = (current_distance-desired_distance)/2

    print("The arm will " + action + str(distance) + " cm " + direction)

else:
    print("The desired distance is out of the accepted limits")
