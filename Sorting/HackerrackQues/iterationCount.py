# Challenge
# Can you modify your previous Insertion Sort implementation to keep track of the number of shifts it makes while sorting? 
# The only thing you should print is the number of shifts made by the algorithm to completely sort the array. 
# A shift occurs when an element's position changes in the array. Do not shift an element if it is not necessary.

# Function Description

# Complete the runningTime function in the editor below.

# runningTime has the following parameter(s):

# int arr[n]: an array of integers
# Returns

# int: the number of shifts it will take to sort the array

# Sample Input

# STDIN       Function
# -----       --------
# 5           arr[] size n =5
# 2 1 3 1 2   arr = [2, 1, 3, 1, 2]
# Sample Output

# 4
# Explanation

# Iteration   Array      Shifts
# 0           2 1 3 1 2
# 1           1 2 3 1 2     1
# 2           1 2 3 1 2     0
# 3           1 1 2 3 2     2
# 4           1 1 2 2 3     1

# Total                     4

def runningTime(arr):
    count = 0
    for i in range(len(arr)):
        j = i
        while(j > 0 and (arr[j-1] > arr[j])):
            count += 1
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
    return count

result = runningTime([2, 5, 1, 4, 7, 8, 3, 9])
print(result)