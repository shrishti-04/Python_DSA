# You are given a list of N numbers and Q queries. Each query is specified by two numbers i and j; 
# the answer to each query is the sum of every number between the range [i, j] (inclusive).

# Note: the query ranges are specified using 0-based indexing.

# Input
# The first line contains N, the number of integers in our list (N ≤ 100,000). 
# The next line holds N numbers that are guaranteed to fit inside an integer. 
# Following the list is a number Q (Q ≤ 10,000). The next Q lines each contain two numbers i and j which specify a query you must answer 
# (0 ≤ i, j ≤ N-1).

# Output
# For each query, output the answer to that query on its own line in the order the queries were made.

def cumulativeSumQuery(arr, queries):
    results = []
    for query in queries:
        i, j = query
        currentSum = 0
        for k in range(i, j+1):
            currentSum += arr[k]
        results.append(currentSum)
    return results

ans = cumulativeSumQuery([1, 2, 3, 4, 5], [(1, 3), (0, 4), (2, 4)])
print(ans) # [9, 15, 12]

# Time Complexity: O(N * Q)

# Optimized Approach by Hashing

def cumulativeSumQuery(arr, l, r):
    n = len(arr)
    prefixSum = [0] * (n+1)

    for i, val in enumerate(arr):
        prefixSum[i+1] = prefixSum[i] + val

    return prefixSum[r+1] - prefixSum[l]

ans = cumulativeSumQuery([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3)
print(ans)
