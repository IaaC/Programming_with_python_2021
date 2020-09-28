#------
#city_area = 641
#city_density = city_population/city_area
#print('...............................................\n')
#print(city_name + ' is the capital of Chile \n')

#area = str(city_area)
#population = str(my_city_population)
#density = str(city_density)

#print('...............................................\n')
#print("The population of "+ city_name + " is " + (population) + " million")
#print("The area of " + city_name + " is " + (area) + " square kilometers")
#print("The density of " + city_name +" is " + density)
#------
my_city_name = "Santiago de Chile"
my_city_population = 5600000
my_previous_city_name = "Talca"
my_previous_city_population = 500000

print('...............................................\n')
if my_city_population > 10000000:
    print("My city is a mega city")
elif my_city_population > 1500000:
    print("My city is a large metropolitan area")
    if my_city_population > my_previous_city_population:
        print("My city is bigger than the previous")
elif my_city_population > 500000:
    print("My city is a metropolitan area")
    if my_city_population > my_previous_city_population:
        print("My city is bigger than the previous")
elif my_city_population > 200000:
    print("My city is a medium size urban area")
    if my_city_population > my_previous_city_population:
        print("My city is bigger than the previous")
elif my_city_population > 50000:
    print("My city is a small urban area")
    if my_city_population > my_previous_city_population:
        print("My city is bigger than the previous")
else:
    print("My city is not a Megacity")
print('...............................................\n')

#Megacity > 10000000
#Large Metropolitan area > 1500000
#Metropolitan Area > 500000
#Medium size urban area > 200000
#Small urban area > 50000
