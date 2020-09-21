##################################################
# This is the first exercise of the 2020 Programming Pre-course at IAAC.
# It briefly describes the author's city.
##################################################
# Author: Alexandra Timageni
# Maintainer: Alexandra Timageni
# Email: alexandra.timageni@studens.iaac.net
# Status: development
##################################################

city_name = 'Athens'
city_population = 3090508
city_area = 364.2
city_density = round(city_population/city_area)
country_population = 10720000
city_population_perc = city_population * 100 / country_population

# Use str() to print a variable with text.

print("  " + city_name + ' in numbers!\n')
print('Today the' + ('\033[2;32;1m population\033[2;32;1m') + ('\033[0;37;1m of the city is ') + str(city_population) +
      ' which is the ' + str(round(city_population_perc)) + '% of the' + ('\033[2;32;1m country\'s total population\033[2;32;1m') +
      ('\033[0;37;1m.') )
print('The' + ('\033[2;32;1m density\033[2;32;1m') + ('\033[0;37;1m of the city is: ') + str(city_density) + ' people/km2.\n')

tourists_2012 = 2500000
tourists_2019 = 6400000
tourists_increase = (tourists_2019-tourists_2012) * 100 / tourists_2019
tourists_per_resident = tourists_2019 / city_population

print(city_name + ' economy is mainly based on tourism.')
print('In 2012, ' + str(tourists_2012) + ('\033[2;32;1m visitors\033[2;32;1m') +
      ('\033[0;37;1m arrived at Eleftherios Venizelos airport, whereas in 2019 came ') + str(tourists_2019) +
      ('\033[2;32;1m visitors\033[2;32;1m') + ('\033[0;37;1m.'))
print('In ' + str(2019-2012) + ' years the number of' + ('\033[2;32;1m visitors\033[2;32;1m') + ('\033[0;37;1m increased by ') +
      str(round(tourists_increase)) + ('%.'))
print('Today each permanent resident of ' + city_name + ' coresponds to ' + str(round(tourists_per_resident)) + ('\033[2;32;1m tourists.\033[2;32;1m'))

