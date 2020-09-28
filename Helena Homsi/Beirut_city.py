# encoding: utf-8

##################################################
# This script shows an example of variable assignment. It explores the different options for storing vales into
# variables
##################################################
#
##################################################
# Author: Helena Homsi
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# Master:  Master in Robotics and Advanced Construction
# Email: helena.homsi@students.iaac.net
# Status: Student
##################################################

# We don't need any library so far

# Let's write our code

# Info about Beirut

city_name = "Beirut"
city_population = 361000
city_area = 19.8
city_summer_temp = 35
city_winter_temp = 9
city_autumn_temp = 18
city_spring_temp = 22
city_universities = 25
city_schools = 41
city_delivery_per_day = 12000
city_traffic_factor = 12500
city_airlines = 38
city_airlines_flights = 3

# Let's check the density of Beirut
city_density = city_population/city_area

print("I am from " + city_name + "\n")
print("Density of Beirut:")
print("There are " + str(city_density) + " people per squared km \n")

# Let's check the average temperature in Beirut
city_temp = (city_summer_temp + city_winter_temp + city_autumn_temp + city_spring_temp)/4

print("Average temperature in Beirut:")
print(str(city_temp) + "°\n")

# Let's check the education sector in Beirut
city_education = (city_universities + city_schools)

print("Education sector in Beirut:")
print("There are " + str(city_education) + " learning institutes in Beirut\n")

# Let's check how much time it takes for food to be delivered in Beirut
city_delivery = (city_delivery_per_day + city_population)/city_traffic_factor

print("Delivery average time in Beirut:")
print("It takes approximately " + str(city_delivery) + " minutes for food to be delivered\n")

# Let's check how many flights land in Beirut every day
city_flights = (city_airlines * city_airlines_flights)

print("Average number of flights landing in Beirut:")
print("There are about " + str(city_flights) + " flights a day\n")

