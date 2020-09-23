my_city = 'Ankara'
my_city_population = 5639076
my_previous_city_name = 'Barcelona'
my_previous_city_population = 5500000




if my_city_population > 10000000:
    print('my city is a Megacity')
elif my_city_population > 1500000:
    print ("my city is large metropolitan area")
    if my_city_population > my_previous_city_population:
        print("my city is bigger than the previous")
    else:
        print('my previouscity is current than the previous one')

elif my_city_population > 500000:
    print ("my city is  metropolitan area")
elif my_city_population > 200000:
    print ("my city is a medium size metropolitan area")
elif my_city_population > 50000:
    print ("my city is asmall urban area")
else:
    print("my city is smaller than a small urban area")

