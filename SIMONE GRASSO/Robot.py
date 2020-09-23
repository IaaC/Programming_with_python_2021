##################################################
# Author: Simone Grasso
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Simone Grasso
# Email: simone.grasso@students.iaac.net
# Status: student
##################################################

d_distance = float(2.0)

#DeltaX = variazione di distanza in movimento

if d_distance > 10:
    print('fast è la velocità''3 è il DeltaX')
elif d_distance > 5:
    print('same speed è la velocità''3 è il DeltaX')
elif 3 < d_distance < 6:
    print('slow è la velocità ' ' 1.5 è il DeltaX')
elif d_distance <= 3:
    print('stop')



