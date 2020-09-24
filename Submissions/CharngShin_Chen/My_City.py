# CharngShin Chen's practice for programming session of IaaC pre-course


##################################################
# Author: CharngShin Chen
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: CharngShin Chen
# Email: charngshin.chen@students.iaac.net
# Status: development
##################################################
import datetime
today = datetime.datetime(2020, 9, 20, 15, 30, 30)

city_name='Taichung'
city_area=22148968
city_population=2816792
city_density=city_population/city_area
print('....................\n')
#Basic
print(str(city_name)+"   "+str(city_area)+" "+'Square kilometers\n')
print('1.'+'Population Density:')
print("  "+str(city_density))
print('....................\n')

#Postion
print('2.'+'Location:')
print("  "+'the middle area of Taiwan(R.O.C)')
print('....................\n')

#Culture
print('3.'+'City Icon')
print("  "+'city flower:Prunus serrulata')
print("  "+'city tree:Pinus morrisonicola')
print("  "+'city bird:Heterophasia auricularis')
print('....................\n')

#Descrition
print('4.'+'Additional:')
print("  "+'- Taichung city has many rivers surrounded with willow and the planning system of the city developed by japanese, so people says the city is the Kyoto of Taiwan. ')
print("  "+'- The industrial characteristics in this city is precise manufacturing. The representative company is Giant Manufacturing Co. which makes good bicycles around the world.')
print('....................\n')

#Time
print('* last edited:'+str(today))