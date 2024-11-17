# An integer s is a divisor of an integer n if the remainder of n / d = 0.

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
# Count the number of divisors occurring within the integer.

# Example
# n = 124

# Check whether 1, 2 and 4 are divisors of 124. All 3 numbers divide evenly into 124 so return 3.

# n = 111
# Check whether 1, 1, and 1 are divisors of 111. All 3 numbers divide evenly into 111 so return 3.

# n = 10
# Check whether 1 and 0 are divisors of 10. 1 is, but 0 is not. Return 1.

# Mathematical approach

def findDigits(n):
    count = 0
    num = n
    
    while(n > 0):
        last_digit = n % 10
        if((last_digit != 0) and (num % last_digit == 0)):
            count += 1
            
        n = n // 10
    
    return count

result = findDigits(36)
print(result)
    
# String-Based Approach

def findDigits(n):
    count = 0
    for i in str(n):
        if(i != '0' and n % int(i) == 0):
            count += 1
    return count

result = findDigits(372)
print(result)