#################################################
# This script is the first exercise for the 2020 Programming pre-course at IAAC.
# It is a brief description of the birth city of the author.
# All information used was based on internet research.
##################################################
#
##################################################
# Author: Alexandra Timageni
# Email: alexandra.timageni@students.iaac.net
# Status: development
##################################################

city_name = 'Athens'
city_population = 2664776
city_area = 7381
barcelona_population = 5575000
luxembourg_population= 122273
ath_brc_population = round(barcelona_population / city_population)
ath_lux_population = round(city_population/luxembourg_population)
city_density = round(city_population/city_area)
metropolitan_population = 3753783
country_population = 10724599
population_met_percentage = round(100 * city_population / metropolitan_population)
population_country_percentage = round(100 * city_population / country_population)

print(city_name + ' in numbers!\n')

# use str() to convert a number into a string
# use \ to run ' as a text

print('Today ' + city_name + '\033[2;32;1m population\033[2;32;1m' + "\033[0;37;1m is " + str(city_population) +
      ', which is the '+ str (population_met_percentage) + '% of the' + '\033[2;32;1m metropolitan population\033[2;32;1m' +
      "\033[0;37;1m and " + str(population_country_percentage) + '% of the country\'s' + '\033[2;32;1m total population' + "\033[0;37;1m.")
print("\033[0;37;1mThe " + '\033[2;32;1m population density\033[2;32;1m' + "\033[0;37;1m of the city is: " + str(city_density) + " people/km^2.\n")


# !!! luxembourg_population isn't working !!!


print(city_name + '\033[2;32;1m population\033[2;32;1m' "\033[0;37;1m is " + str(ath_brc_population) + ' times smaller than Barcelona and ' +
      str(luxembourg_population) + ' times larger than Luxembourg.\n')

tourists_2012 = 2500000
tourists_2019 = 6300000
tourists_inc = ((tourists_2019-tourists_2012)*100) / tourists_2019
population_and_tourism = tourists_2019/city_population

print('The economy of the city is mainly based on tourism.')
print('In 2012, ' + str(tourists_2012) + '\033[2;32;1m visitors\033[2;32;1m' +
      '\033[0;37;1m arrived at Eleftherios Venizelos airport, whereas in 2019 arrived ' + str(tourists_2019) + '.')
print('In ' + str(2019-2012) + ' years there was an ' + str(round(tourists_inc)) + ' %' + '\033[2;32;1m increase\033[2;32;1m'+
      "\033[0;37;1m in the number of visitors.")
print('Each permanent resident corresponds to ' + str(round(population_and_tourism)) + ' visitors (2019 data).')
