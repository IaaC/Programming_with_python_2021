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

# End of header section

my_previous_city_name = 'Catania'
my_previous_city_population = 1116000

my_city_name = 'Barcelona'
my_city_population = 5500000

if my_city_population > 10000000:
    print('my city is a megacity')
elif my_city_population > 1500000:
    print('my city is a large metropolitan area')
    if my_city_population > my_previous_city_population:
        print ('my city is bigger than the previous')
    else:
        print('my previous city is bigger than the current city')
elif my_city_population > 500000:
    print('my city is a metropolitan area')
elif my_city_population > 200000:
    print('my city is a medium size urban area')
elif my_city_population > 50000:
    print('my city is a small urban area')
else:
    print('my city is neither a mega city nor a large metropolitan area')

print('end of script')

