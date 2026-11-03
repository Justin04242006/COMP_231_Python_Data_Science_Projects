# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Loading the Tromso 2024 historical data csv file using a numpy ufunc

import numpy as np

Tromso_2024_weather_data=np.genfromtxt("/Users/justinpeabody/Desktop/COMP_231/In_class_data_projects/COMP_231_Data_Science_Mini_Projects/tromso.csv", delimiter=",", skip_header=1)

#Column 0 = the date (as expected, it was filled with NaN values because numpy csv import ufuncs expect all values in the file to be the same data type), Column 3 = maximum temperatures, Column 2= minimum temperature, Column 4 = total precipitation, Column 5=snow depth

#Question 1: How many days out of the year is there precipitation?

Precipitation_array=Tromso_2024_weather_data[:, 4]

Num_days_with_precipitation=np.sum(Precipitation_array > 0) #Computes the number of rows (days) with precipitation values greater than zero
print(Num_days_with_precipitation)
#237 days in 2024 experienced some form of precipitation (rain, snow, or otherwise).




#Question 2: What is the average and standard deviation of precipitation (in inches, not mm) in 2024?

#Precipitation values are currently in millimeters, so I need to convert them to inches by dividing by 25.4

Precipitation_values_inches=np.divide(Precipitation_array, 25.4)

Average_precip_inches=np.mean(Precipitation_values_inches)
Standard_deviation_precip_inches=np.std(Precipitation_values_inches)

print(Average_precip_inches)
print(Standard_deviation_precip_inches)

#Mean of 0.145 inches, standard deviation of 0.236 inches (rounded)




#Question 3: How many days was there snow on the ground per month?

Snow_depth_array=Tromso_2024_weather_data[:, 5]

#I will create a new smaller array for the snow depth within each month

start_indices=[0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366] #Index positions corresponding to each month in the dataset
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

num_days_nonzero_snow_depth=[] #Creating a list of tuples in which each tuple contains the numeric month (from 1 thru 12) and the number of days in this month with nonzero snow depth
for i in range(len(months)):
    start=start_indices[i]
    end=start_indices[i+1]
    new_snow_depth_array=Snow_depth_array[start:end] #Creating a new array that is a subset of the 1 dimensional snow depth array, subsetted to include elements form the month in question
    num_days_snow_on_ground=np.sum(new_snow_depth_array > 0)
    tup=(months[i], int(num_days_snow_on_ground))
    num_days_nonzero_snow_depth.append(tup)
print(num_days_nonzero_snow_depth)


#January: 31 days
#February: 29 days
#March: 31 days
#April: 30 days
#May: 10 days
#June: 0 days
#July: 0 days
#August: 0 days
#September: 0 days
#October: 3 days
#November: 22 days
#December: 31 days




#Question 4: What was the maximum snow on the ground per month?

max_snow_cover_monthly=[] #Creating a list of tuples in which each tuple contains the numeric month (from 1 thru 12) and the maximum snow depth in that month
for i in range(len(months)):
    start=start_indices[i]
    end=start_indices[i+1]
    new_snow_depth_array=Snow_depth_array[start:end] #Creating a new array that is a subset of the 1 dimensional snow depth array, subsetted to include elements form the month in question
    max_snow_depth=np.max(new_snow_depth_array)
    tup=(months[i], int(max_snow_depth))
    max_snow_cover_monthly.append(tup)
print(max_snow_cover_monthly)

#January: 93 mm
#Feburary: 127 mm
#March: 103 mm
#April: 97 mm
#May: 37 mm
#June: 0 mm
#July: 0 mm
#August: 0 mm
#September: 0 mm
#October: 10 mm
#November: 59 mm
#December: 91 mm




#Question 5: What was the minimum and maximum recorded temperature per month?


###Minimum recorded temperature per month

minimum_temp_array=Tromso_2024_weather_data[:, 2]

min_temp_by_month=[] #Creating a list of tuples in which each tuple contains the numeric month (from 1 thru 12) and the maximum snow depth in that month
for i in range(len(months)):
    start=start_indices[i]
    end=start_indices[i+1]
    new_min_temp_array=minimum_temp_array[start:end] #Creating a new array that is a subset of the 1 dimensional snow depth array, subsetted to include elements form the month in question
    min_temp=np.min(new_min_temp_array)
    tup=(months[i], float(min_temp))
    min_temp_by_month.append(tup)
print(min_temp_by_month)


#January: -13.5 C
#Feburary: -12.3 C
#March: -7.7 C
#April: -11.5 C
#May: -2.0 C
#June: 5.6 C
#July: 7.6 C
#August: 8.6 C
#September: -0.4 C
#October: -3.6 C
#November: -8.5 C
#December: -10.1 C


###Maximum recorded temperature per month

maximum_temp_array=Tromso_2024_weather_data[:, 3]

max_temp_by_month=[] #Creating a list of tuples in which each tuple contains the numeric month (from 1 thru 12) and the maximum snow depth in that month
for i in range(len(months)):
    start=start_indices[i]
    end=start_indices[i+1]
    new_max_temp_array=maximum_temp_array[start:end] #Creating a new array that is a subset of the 1 dimensional snow depth array, subsetted to include elements form the month in question
    max_temp=np.max(new_max_temp_array)
    tup=(months[i], float(max_temp))
    max_temp_by_month.append(tup)
print(max_temp_by_month)


#January: 7.7 C
#Feburary: 6.2  C
#March: 7.6 C
#April: 9.5 C
#May: 26.6 C
#June: 23.5 C
#July: 28.5 C
#August: 26.9 C
#September: 23.4 C
#October: 13.8 C
#November: 11.4 C
#December: 5.3 C



        