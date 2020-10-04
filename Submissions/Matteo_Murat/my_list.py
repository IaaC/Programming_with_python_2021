

names = ['Turin', 'Lecce', 'Bologna','Oporto','Madrid', 'Barcelona']

population = [6500000, 15000, 5500000, 3000000, 6000000, 300000,]

cities = [names, population]

number_of_cities = len(names)
print(number_of_cities)

#-----------------------------
#for i in range (number_of_cities): #to have names of cities one under the other
#    print (cities[i])

#if number_of_cities >= 3:
#    print(cities)
#else:
#    print(str('you have '), number_of_cities, str('cities'))
#----------------------------

print(cities)
print(cities[0][4])

print('the city of ', cities[0][0], 'has ', cities [1][0], 'inhabitants')

for i in range(number_of_cities):
    print(cities[0][i], 'has a population of', cities [1][i])