# # In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

# Function Description

# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

# aVeryBigSum has the following parameter(s):

# int ar[n]: an array of integers .
# Return

# long: the sum of all array elements
# Input Format

# The first line of the input consists of an integer n.
# The next line contains n space-separated integers contained in the array.

# Output Format

# Return the integer sum of the elements in the array.

# Sample Input

# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# Output

# 5000000015

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

ar_sum = 0
for i in ar:
    ar_sum += i
            
print(ar_sum)