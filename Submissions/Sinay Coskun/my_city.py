my_city= "Ankara"
population = 5639076
area = 24521
density = population/area

print(f"population density of {my_city} is {density:.2f}")

#here is another way

print("Population density of " + my_city +  " is " + str(density))

#one final way
print("Population density of %s is %.2f " %(my_city,density))
