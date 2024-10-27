# Staircase detail

# This is a staircase of size n = 4:

#        #
#       ##
#      ###
#     ####
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size n.

# Function Description

# Complete the staircase function in the editor below.

# staircase has the following parameter(s):

# int n: an integer
# Print

# Print a staircase as described above.

# Input Format

# A single integer, n, denoting the size of the staircase.

n = int(input('Enter your number: '))

for i in range(n):
    print(' '*(n-i), end='')
    print('#' * (i+1))
    
# another method which is also valid

n = int(input('Enter your number: '))

for i in range(n):
    print(' '*(n-i), end='')
    for j in range(i+1):
        print('#', end='')
    print('')