# Find the number of subarrays whose sum is less than equal to k

def subarraySum(nums, k):

    count = 0
    sums = 0
    n = len(nums)

    for i in range(n):
        sums = 0
        for j in range(i, n):
            sums += nums[j]
            if sums <= k:
                count += 1

    return count

print(subarraySum([2, 1, 1, 5, 8], 4))

# Time Complexity: O(n^2)

# Optimized Approach: Using Two Pointer Technique

def subarraySum(nums, k):

    count = 0
    sums = 0
    n = len(nums)
    i = 0

    for j in range(n):
        sums += nums[j]

        while(sums >= k):
            sums -= nums[i]
            i -= 1

        count += j - i + 1

    return count

print(subarraySum([2, 1, 1, 5, 8], 4))