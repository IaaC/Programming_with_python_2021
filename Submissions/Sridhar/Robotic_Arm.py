# encoding: utf-8

##################################################
# This script is to try Conditional commands.
##################################################
#
##################################################
# Author: Sridhar Subramani
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Sridhar Subramani
# Email: sridhar.subramani@students.iaac.net
# Status: development
##################################################


desired_distance = int(input("Desired distance(0-5): "))
distance = int(input("Distance to the object: "))
default_move = 3

if distance > 10:
    print('MOVE FASTER')
elif distance > 5:
    print('SAME SPEED')
elif distance > desired_distance:
    print('REDUCE SPEED')
else:
    print('STOP')


if distance < 3:
    move = (distance - desired_distance)/2
    print('moving '+ str(move)+ ' cm')
elif distance < desired_distance:
    print('moving backward')
else:
    print('moving 3 cm ahead')



