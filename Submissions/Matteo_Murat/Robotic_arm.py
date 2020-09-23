# encoding: utf-8

##################################################
# Author: Matteo Murat
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Matteo Murat
# Email: matteo.murat@students.iaac.net
# Status: development
##################################################

# End of header section

desidered_distance = 4
distance_1 = 5
distance_2 = 10
current_distance = 2

print('the current distance is: ')
print(current_distance)

if current_distance >= distance_2:
    print('so the robotic arm will move faster')
    print('move 3 forward')
elif current_distance > distance_1:
    print('so the robotic arm will move at the same speed')
    print('move 3 forward')
elif desidered_distance <= current_distance <= distance_1:
    print('so the robotic arm will move slower')
    if current_distance < 3:
        distance_to_move = (current_distance-desidered_distance) / 2
        print('the distance to move is:' + distance_to_move)
        print(distance_to_move)
elif current_distance <= desidered_distance:
    print('so the robotic arm will stop')





