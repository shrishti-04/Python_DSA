# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal = 1+5+9 = 15 The right to left diagonal = 3+5+9 = 17 Their absolute difference is |15 - 17| = 2

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference

arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

row = len(arr)
col = row - 1

sum1 = 0
sum2 = 0

for i in range(row):
    
    sum1 = sum1 + arr[i][i]
    sum2 = sum2 + arr[i][col]
    col -= 1
    
print(abs(sum1 - sum2))