# Number of subarrays whose count of distinct number <= K

def subarraySum(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        g = {}
        for j in range(i, n):
            g[nums[j]] = g.get(nums[j], 0) + 1
            d = len(g)
            if(d <= k):
                count += 1

    return count

print(subarraySum([2, 1, 1, 5, 8], 4))

# Time Complexity: O(n^2)

# Optimized Approach: Using Two Pointer Technique

def subarraySum(nums, k):
    n = len(nums)
    count = 0

    i = 0
    for j in range(i, n):
        g = {}
        g[nums[j]] = g.get(nums[j], 0) + 1
        d = len(g)
        while(d > k):
            g[nums[i]] -= 1
            if(g[nums[i]] == 0):
                del g[nums[i]]
            i += 1
        count += j - i + 1

    return count

print(subarraySum([2, 1, 1, 5, 8], 4))