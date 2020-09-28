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

print('These are prime numbers: \n')

for i in range(2, 100):
    number = 2
    prime = True
    while prime and number < i:
        if i % number == 0:
            prime = False
        else:
            number = 1
        if prime:

            print(i, 'es primo')
