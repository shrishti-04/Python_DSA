# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Bruteforce Approach

def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if(i != j and arr[i] + arr[j] == target):
                return [i, j]
            
ans = twoSum([2,7,11,15], 9)
print(ans)

# Hashing Approach

def twoSum(arr, target):

    hash_map = {}

    for i, v in enumerate(arr):
        if(target - v in hash_map):
            return [hash_map[target - v], i]
        hash_map[v] = i

ans = twoSum([2,7,11,15], 9)
print(ans)