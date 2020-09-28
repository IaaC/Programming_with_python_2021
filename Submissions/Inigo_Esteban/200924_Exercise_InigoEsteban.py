# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Inigo Esteban
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: inigo.esteban.marina@iaac.student.net
# Status: development
##################################################
# Try to print prime numbers smaller than 100
##################################################

num_prime = []
for i in range (1,100):
    count_list = []
    for n in range(1,i+1):
        if i % n ==0:
            count_list.append(n)
    if len(count_list) == 2:
        num_prime.append(i)
        print(i)
print(num_prime)

'''
Now I wan to do a new commit to push it from gitkraken
'''
