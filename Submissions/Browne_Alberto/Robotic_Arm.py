##################################################
# Author: Alberto Browne
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Alberto Browne
# Email: alberto.eugenio.browne@students.iaac.net
# Status: development
##################################################

robotic_arm = 2.5
object = 1

if robotic_arm > 10:
    print('move faster and move 3 cm toward')
elif robotic_arm > 5:
    print('move at the same speed and move 3 cm toward')
elif robotic_arm >= 3 < 5:
    print('reduce the speed and move 3 cm toward')
elif robotic_arm < 3:
    result = (robotic_arm - object) / 2
    print('move ' + str(result) + ' cm ' + 'and stop')
    print('............. \n')
    print('end of script')
