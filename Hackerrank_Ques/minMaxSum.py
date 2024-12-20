# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example
# arr = [1, 3, 5, 7, 9]

# The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24. The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of 5 integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

arr = [1, 3, 5, 7, 9]
n = len(arr)
s = sum(arr)
x = []

for i in range(n):
    a = s - arr[i]
    x.append(a)
    
print(min(x), max(x))