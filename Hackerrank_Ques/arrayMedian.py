# The median of a list of numbers is essentially its middle element after sorting. 
# The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, find the median?

# Example
# arr = [5, 3, 1, 2, 4]

# The sorted array arr = [1, 2, 3, 4, 5]. The middle element and the median is 3.

# Function Description

# Complete the findMedian function in the editor below.

# findMedian has the following parameter(s):

# int arr[n]: an unsorted array of integers

def isEven(num):
    num % 2 == 0

def median(arr):
    arr.sort()
    length = len(arr)
    mid = length // 2

    if(isEven(length)):
        result = (arr[mid] + arr[mid-1]) / 2
    else:
        result = arr[mid]

    return result

ans = median([7, 3, 9, 4, 1, 5])
print(ans)
