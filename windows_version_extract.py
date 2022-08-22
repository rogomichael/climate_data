from netCDF4 import Dataset
import numpy as np
import pandas as pd

data=Dataset('year2019.nc','r')
#print(data)

lon = data.variables['longitude'][:]
lat = data.variables['latitude'][:]

#lat_france = 	41.14764
#lon_france = 	-8.58032

lat_france = 	49.375
lon_france = 	8.375


#get squared difference
sq_diff_lat = (lat - lat_france)**2
sq_diff_long = (lon - lon_france)**2

#print("Distance lat..\n", sq_diff_lat)
#print("Distance lon..\n", sq_diff_long)

#Retrieve the index of the minimum value
min_index_lat = sq_diff_lat.argmin()
#print(min_index_lat)
min_index_lon = sq_diff_long.argmin()
#print(min_index_lon)

#Cross-check
#print(sq_diff_lat.min())
#print(sq_diff_lat.min())

temp = data.variables['tg']
#print(temp)
print("Porto Temp", temp[1, 63, 127], temp.units)

#Extract starting date
starting_date= data.variables['time'].units 
#print(starting_date)
starting_date= data.variables['time'].units[11:21]
print("Starting_date:..", starting_date)
ending_date = data.variables['time'].units[11:15] + '-12-31'
print("Ending date:..", ending_date)

date_range = pd.date_range(start = starting_date, end=ending_date)
df = pd.DataFrame(0, columns=['Temperature'], index = date_range)

print("Shape of our dataframe...\n", df.shape)
#print("New Array", new_array)
dt = np.arange(0, data.variables['time'].size)
print(temp[24, min_index_lat, min_index_lon])
