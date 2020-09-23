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

desidered_distance = 4
distance_1 = 5
distance_2 = 10
current_distance = 2

print('the current distance is: ')
print(current_distance)

if current_distance >= distance_2:
    print('so the robotic arm will move faster')
elif current_distance > distance_1:
    print('so the robotic arm will move at the same speed')
elif desidered_distance <= current_distance <= distance_1:
    print('so the robotic arm will move slower')
elif current_distance <= desidered_distance:
    print('so the robotic arm will stop')

move = 3
if current_distance < move:
    distance_to_move = 0.5 * desidered_distance - current_distance
    print('the distance to move is:')
    print(distance_to_move)


