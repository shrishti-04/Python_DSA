# Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

# Examples :

# Input: arr = [1, 1, 1, 1, 1], x = 1
# Output: 5
# Explanation: Frequency of 1 is 5.

def findFrequency(arr, x):
    count = 0
    for i in arr:
        if(i == x):
            count += 1

    return count

arr = [2, 6, 4, 8, 2, 2, 1]
ans = findFrequency(arr, 2)
print(ans)

# Time Complexity: O(n)

# Optimized Approach: Using Hashing

from collections import defaultdict

def findFrequency(arr, x):
    hm = defaultdict(int)

    for i in arr:
        hm[i] = hm.get(i, 0) + 1

    if x in hm:
        return hm[x]
    else:
        return 0
    
arr = [2, 6, 4, 8, 2, 2, 1]
x = 2
ans = findFrequency(arr, x)
print(ans)
    