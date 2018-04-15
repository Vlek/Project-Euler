#problem 19

import time, datetime

sundays = 0

#For each year in the century,
for yearindex in range(1,101):
    #For each month in a given year,

    for monthindex in range(1,13):
        
        if datetime.datetime(1900+yearindex, monthindex, 1).weekday() == 6:
            sundays += 1


print sundays
