# Explanation 0

# In the year y = 2017, January has 31 days, February has 28 days, March has 31 days, April has 30 days, 
# May has 31 days, June has 30 days, July has 31 days, and August has 31 days. When we sum the total number of days 
# in the first eight months, we get 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 = 243. Day of the Programmer is the 256th day, 
# so then calculate 256 - 243 = 13 to determine that it falls on day 13 of the 9th month (September). 
# We then print the full date in the specified format, which is 13.09.2017.

# Explanation 1

# Year  = 2016 is a leap year, so February has 29 days but all the other months have the same number of days as in 2017.
# When we sum the total number of days in the first eight months, we get 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 = 244. 
# Day of the Programmer is the 256th day, so then calculate 256 - 244 = 12 to determine that it falls on day 12 of the 9th month (September). 
# We then print the full date in the specified format, which is 12.09.2016.

def dayOfProgrammer(year):
    
    if(year == 1918):
        print('26.09.'+str(year))
    
    elif(year < 1918):
        if(year % 4 == 0):
            print('12.09.'+str(year))
        else:
            print('13.09.'+str(year))
        
    else:
        if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            print('12.09.'+str(year))
        else:
            print('13.09.'+str(year))
        
dayOfProgrammer(2024)