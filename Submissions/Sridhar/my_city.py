# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Sridhar Subramani
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Sridhar Subramani
# Email: sridhar.subramani@students.iaac.net
# Status: development
##################################################

# End of header section

from datetime import datetime
import pytz
# Have imported a library to test it. Trying to print date and time of the particular location.
# two new library

city_name = 'Bangalore'
city_area = 709
city_population = 8443675
city_density = city_population/city_area
city_establishment = 1537
country = 'India'
state = 'Karnataka'

tz_IN = pytz.timezone('Asia/Calcutta')
datetime_IN = datetime.now(tz_IN)
current_time = datetime_IN.strftime("%H:%M:%S")

print('CITY : ' + city_name.upper())
print('Country: ' + country , 'State: ' + state , sep='\n' )
print('Area in Sq.km: ' + str(city_area))
print('City was established in: ' + str(city_establishment))
print('Population: ' + format(city_population, ',d'))
print('Population Density: ' + str(city_density) + ' per Sq.Km')

print('current time: ' + current_time)

