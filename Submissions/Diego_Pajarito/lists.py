names = ['Bogotá', 'Sasaima', 'Barcelona', 'Lisbon', 'Madrid', 'Valencia', 'Castelló',
          'Pamplona', 'Nantes', 'Donostia']
population = [6500000, 15000, 5500000, 3000000, 6000000, 700000, 300000, 150000, 300000, 80000]

cities = [names, population]


number_of_cities = len(cities)

if number_of_cities >= 10:
    print(cities)
else:
    print('You have less than ten cities')



if number_of_cities >= 10:
    for i in range(number_of_cities):
        print(cities[i])
else:
    print('You have less than ten cities')

for i in cities:
    print(i)


# We can also create list
names = ['Bogotá', 'Sasaima', 'Barcelona', 'Lisbon', 'Madrid', 'Valencia', 'Castelló',
          'Pamplona', 'Nantes', 'Donostia']

population = [6500000, 15000, 5500000, 3000000, 6000000, 700000, 300000, 150000, 300000, 80000]

cities = [names, population]

for i in range(number_of_cities):
    print(cities[0][i], ' has a population of ', cities[1][i])