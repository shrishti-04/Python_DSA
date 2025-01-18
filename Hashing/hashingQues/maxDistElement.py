# Given an array arr[], the task is to find the maximum distance between two occurrences of any element. If no element occurs twice, return 0.

# Examples:  

# Input: arr = [1, 1, 2, 2, 2, 1]
# Output: 5
# Explanation: distance for 1 is: 5-0 = 5, distance for 2 is: 4-2 = 2, So max distance is 5.


# Input : arr[] = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
# Output: 10
# Explanation : Max distance for 2 is 11-1 = 10, max distance for 1 is 4-2 = 2 and max distance for 4 is 10-5 = 5  


# Input: arr[] = [1, 2, 3, 6, 5, 4]
# Output: 0
# Explanation: No element has two occurrence, so maximum distance = 0.

# Bruteforce Approach:

def maxDistElement(arr):
    n = len(arr)
    res = 0

    for i in range(n):
        for j in range(i+1, n):
            if(arr[i] == arr[j]):
                res = max(res, j-i)

    return res

arr = [1, 1, 2, 2, 2, 1]
print(maxDistElement(arr))

# Hashing Approach:

def maxDistElement(arr):
    n = len(arr)
    res = 0

    mp = {}

    for i in range(n):
        if(arr[i] in mp):
            res = max(res, i - mp[arr[i]])
        else:
            mp[arr[i]] = i

    return res

arr = [1, 1, 2, 2, 2, 1]
print(maxDistElement(arr))