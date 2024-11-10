# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example
# a = [2, 6]
# b = [24, 36]

# There are two numbers between the arrays:  and .
# 6%2 = 0, 6%6 = 0, 6%24 = 0 and 6%36 = 0 for the first value.
# 12%2 = 0, 12%6 = 0, 12%24 = 0 and 12%36 = 0 for the second value. Return 2.

# Function Description

# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

# getTotalX has the following parameter(s):

# int a[n]: an array of integers
# int b[m]: an array of integers
# Returns

# int: the number of integers that are between the sets

# Sample Input

# 2 3
# 2 4
# 16 32 96

# Sample Output

# 3

def getTotalX(a, b):

    max_a = max(a)
    max_b = max(b)
    possibilities = 0
    
    for i in range(max_a, max_b + 1):
        good_i = True
        
        for j in a:
            if(i%j != 0):
                good_i = False
                
        for k in b:
            if(k%i != 0):
                good_i = False
                
        if(good_i):
            possibilities += 1
            
    print(possibilities)
    
getTotalX([2, 4], [16, 32, 96])