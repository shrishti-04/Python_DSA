# A modified Kaprekar number is a positive whole number with a special property. 
# If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

# Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2*d digits long or (2*d)-1 digits long. 
# Split the string representation of the square into two parts, l and r. The right hand part, r must be d digits long. 
# The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get n.

# Example
# n = 5
# d = 1

# First calculate that n^2 = 25. Split that into two strings and convert them back to integers 2 and 5. 
# Test 2+5=7 != 5, so this is not a modified Kaprekar number. If n=9, still d=1, and n^2 = 81. 
# This gives us 8+1=9, the original n.

# In mathematics, a Kaprekar number for a given base is a non-negative integer,
# the representation of whose square in that base can be split into two parts that add up to the original number again.
# For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.

def kaprekarNum(p, q):
    result = []
    
    for i in range(p, q+1):
        d = len(str(i))
        square = str(i**2)
        
        left = square[-d:]
        right = square[:-d]
        
        left = int(left) if left else 0
        right = int(right) if right else 0
        
        if(left + right == i):
            result.append(i)
            
    if(result):
        print(' '.join(map(str, result)))
    else:
        print('INVALID RANGE')
        
kaprekarNum(1, 100)