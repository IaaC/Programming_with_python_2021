# encoding: utf-8

##################################################
# MyCity class contain city information and process the density.
##################################################
#
##################################################
# Author: Tugdual Sarazin
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Tugdual Sarazin
# Email: tugdual.sarazin@students.iaac.net
# Status: development
##################################################

class MyCity:
    def __init__(self, name: str, area: float, population: int):
        """

        :param name: name of the city
        :param area: square kilometers of the city
        :param population: number of inhabitants
        """
        self.name = name
        self.area = area
        self.population = population

    def density(self) -> float:
        """

        :return: density of population (inhabitants per km2)
        """
        return self.population / self.area

    def __str__(self):
        return 'City(name={name}, area={area} km2, population={pop} hab, density()={density} hab/km2)'.format(
            name=self.name, area=self.area, pop=self.population, density=round(self.density(), 2))


paris = MyCity(name='Paris', area=105.4, population=2148271)
print(paris)
