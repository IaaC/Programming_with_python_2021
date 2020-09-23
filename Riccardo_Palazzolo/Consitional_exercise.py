##################################################
# Author: Riccardo Palazzolo Henkes
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Riccardo Palazzolo Henkes
# Email: riccardo.palazzolo@students.iaac.net
# Status: development
##################################################

# End of header section

#First Decision
current_distance = 1
desired_distance = 2
#If distance is bigger than 10 cm then move faster
if current_distance > 10:
    print('move faster')
elif current_distance > 5:
    print('move at the same speed')
elif current_distance > desired_distance:
    print('reduce the speed')
else:
    print('stop')

#second Decision
result = current_distance - desired_distance
print(result)
if result < 3:
    move1 = result / 2
    print(move1)
