
my_city_name = "Naples"
my_city_population = 200000
my_previous_city_name = "Barcelona"
my_previous_city_population = 100000

if my_city_population > 10000000:
    print('My city is a Mega Metropolitan City')
elif my_city_population > 1500000:
    print('My city is a Large Metropolitan City')
    if my_city_population > my_previous_city_population:
        print('My city is bigger than the previous')
    else:
        print('My city is smaller than my previous')
elif my_city_population > 500000:
    print('My city is a Metropolitan City')
else:
    print('My city is a Medium Urban City')
