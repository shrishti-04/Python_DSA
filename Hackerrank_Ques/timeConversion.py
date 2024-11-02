# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example

# s = '12:01:00PM'
# Return '12:01:00'

# s = '12:01:00AM'
# Return '00:01:00'

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in 12 hour format
# Returns

# string: the time in 24 hour format
# Input Format

# A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

def timeConversion(s):
    if(s[-2:] == 'AM'):
        if(s[:2] == '12'):
            return '00'+s[2:]
        else:
            return s[:8]
        
    else:
        if(s[:2] == '12'):
            return s[:8]
        else:
            num = int(s[:2]) + 12
            return str(num) + s[2:8]
        
print(timeConversion('02:00:00PM'))
print(timeConversion('12:00:00AM'))
print(timeConversion('01:00:00AM'))