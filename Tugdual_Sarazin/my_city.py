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
from Tugdual_Sarazin.city_size_type import MegaCity, LargeMetropolitan, SmallUrbanArea, MediumCity, Metropolitan, \
    CitySizeType


class MyCity:
    __CITY_SIZE_TYPES__ = [MegaCity(), LargeMetropolitan(), Metropolitan(), MediumCity(), SmallUrbanArea()]

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

    def size_type(self) -> CitySizeType:
        """

        :return: size type object of the object
        """
        max_size_type = None
        for size_type in self.__CITY_SIZE_TYPES__:
            if self.population > size_type.min_size:
                if max_size_type is None:
                    max_size_type = size_type
                elif size_type.min_size > max_size_type.min_size:
                    max_size_type = size_type
        return max_size_type

    def __str__(self):
        return f"City(name={self.name}, area={self.area} km², population={self.population} hab, density()={round(self.density(), 2)} hab/km², size_type()='{self.size_type().name}')"


def tests_my_city():
    # Test density
    basic_city = MyCity(name='Basic', area=2, population=10)
    assert basic_city.density() == 5

    # Test size_type
    mega_city = MyCity(name='Mega', area=1, population=10000001)
    assert type(mega_city.size_type()) == MegaCity
    almost_mega_city = MyCity(name='LargeMetropolitan', area=1, population=10000000)
    assert type(almost_mega_city.size_type()) == LargeMetropolitan
    small_city = MyCity(name='Small', area=1, population=1)
    assert type(small_city.size_type()) == SmallUrbanArea

    # Test __str__
    # print(str(basic_city))
    assert str(basic_city) == "City(name=Basic, area=2 km², population=10 hab, density()=5.0 hab/km², size_type()='Small urban area')"


def main():
    paris = MyCity(name='Paris', area=105.4, population=2148271)
    print(paris)


if __name__ == '__main__':
    tests_my_city()
    # main()
