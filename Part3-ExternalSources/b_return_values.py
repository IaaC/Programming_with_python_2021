# encoding: utf-8

##################################################
# This script shows an example of a script using functions as a way to simplify programming.
# This functions can also return more than one value
#
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We don't need libraries for this script


##################################################
# We have a temporal section for defining functions

def get_proportions(values, names, label):
    answer_template = '%s from %s is %f times %s from %s'
    proportions = []
    proportions.append(round(values[0] / values[1], 1))
    proportions.append(round(values[0] / values[2], 1))
    proportions.append(round(values[1] / values[2], 1))

    print(answer_template % (label, names[0], proportions[0], label, names[1]))
    print(answer_template % (label, names[0], proportions[1], label, names[2]))
    print(answer_template % (label, names[1], proportions[2], label, names[2]))



def get_averages(values1, values2):
    average1 = sum(values1) / len(values1)
    average2 = sum(values2) / len(values2)
    return average1, average2


##################################################
# and now we have the section for our source code
cities = {'names': ['Barcelona', 'Lisbon', 'Amsterdam'],
          'population': [5474482, 2827514, 2431000],
          'unemployment_rate': [17.24, 7.4, 3.3],
          'gdp_billions': [173, 72, 154]}
text_template = 'Average population is: %f \n Average unemployment rate is: %f'

val1, val2 = get_averages(cities['population'], cities['gdp_billions'])

#print(text_template % (val1, val2))

# This function prints the city names and GDP values using a template. Check it out above
get_proportions(cities['gdp_billions'], cities['names'], 'GDP')


# Now we proceed to calculate the GDP per capita. First, we create an empty list and lists for population and GDP
per_capita = []
gdp_billions =  cities['gdp_billions']
population = cities['population']
# Ths for loop goes across cities
for i in range(len(cities['gdp_billions'])):
    # Here we transform GDP units from billions to millions. 1b = 1000m
    gdp_mill = cities['gdp_billions'][i] * 1000
    # Here we transform population to millions. 1m = pop / 1000000
    pop_mill = population[i] / 1000000
    gdp_percapita = gdp_mill / pop_mill
    per_capita.append(gdp_percapita)

# We print the list in which we appended all individual values
print(per_capita)

# See this formula as an exmaple of GDP per capita estimation
#cities['gdp_percapita'] = ( cities['gdp_billions'] * 1000 ) / ( cities['population'] / 1000000)


#######################
# Side note, calling lists within lists. It works also for dictionaries.
my_list = [["a","b","c"],["d","e","f"]]

# print first item of second list in my_list
print (my_list[1][0])
