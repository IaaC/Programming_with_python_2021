# End of header section


my_city_name = 'Barcelona'
my_city_population = 5500000
my_previous_city_name = 'Patras'
my_precious_city_population = 168000

if my_city_population > 10000000:
    print ('My city is a Megacity')
elif my_city_population > 1500000:
    print ('My city is a Large Metropolitan Area')
    if my_city_population > my_precious_city_population:
        print ('My city is bigger than the previous')
    else:
        print ('My previous city is bigger than the current one')
elif my_city_population > 500000:
    print ('My city is a Metropolitan Area')
elif my_city_population > 200000:
    print ('My city is a Medium Size Urban Area')
elif my_city_population > 50000:
    print ('My city is a Small Urban Area')
else:
    print ('My city is smaller than a small Urban Area')











#Megacity > 10.000.000
#Large Metropolitan Area > 1.500.000
#Metropolitan Area > 500.000
#Medium Size urban area > 200.000
#Small Urban Area > 50.000