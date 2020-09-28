
my_city_name = 'Athens'
my_city_population = 2000000
new_city_name= 'Barcelona'
new_city_population = 5500000

if my_city_population > 10000000:
    print('My city is a Megacity.\n')

elif my_city_population > 1500000:
    print('My city is a Metropolitan area.\n')


elif my_city_population < 1500000:
    if my_city_population > 599999:
        print('My city is a Metropolitan area')
    elif my_city_population > 20000:
        print('My city is a small urban area.')

if my_city_population > new_city_population:
        print('My city is bigger than Barcelona')
else:
        print('My city is smaller than Barcelona.')
