names = ['Barcelona','new york', 'san fransico' , 'Berlin' , 'ibiza' , 'Sao paulo' , 'naples' , 'buenos Aires' ,
          'Rio De Janeiro' , 'Buffalo' ]

population = 5, 8, 7, 4, .02, 15, 5, 6, 3, .08

cities = [population, names]









number_of_cities = len(cities)

if number_of_cities <= 10:
    for i in range(number_of_cities):
        print(cities[i])
else:
    print('you have less than 10 cities')

