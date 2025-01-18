# This was the question asked in Amazon interview for 45 LPA package
# And the question was to find maximum prefix suffix subarray sum in an array which are not contain overlapping elements

# Amazon Interview Question Solution

def maxSubarrayPrefixSum(b):
    n = len(b) - 1
    if(n == 0):
        return 0
    
    prefixSum = [0] * (n + 1)
    currentMax = b[1]
    prefixSum[1] = b[1]

    for i in range(1, n+1):
        currentMax = max(currentMax + b[i], b[i], 0)
        prefixSum[i] = currentMax

    return prefixSum

def maxSubarraySuffixSum(b):
    n = len(b) - 1
    if(n == 0):
        return 0
    
    suffixSum = [0] * (n + 1)
    currentMax = b[n]
    suffixSum[n] = b[n]

    for i in range(n-1, 0, -1):
        currentMax = max(currentMax + b[i], b[i], 0)
        suffixSum[i] = currentMax

    return suffixSum

def maxSubarraySum(b):
    n = len(b) - 1

    if(n == 0):
        return 0

    prefixMaxSum = maxSubarrayPrefixSum(b)
    suffixMaxSum = maxSubarraySuffixSum(b)

    maxprefix = [0]*(n+2)
    maxprefix[1] = prefixMaxSum[1]
    for i in range(2, n):
        maxprefix[i] = max(maxprefix[i-1], prefixMaxSum[i])

    maxsuffix = [0]*(n+2)
    maxsuffix[n] = suffixMaxSum[n]
    for i in range(n-1, 0, -1):
        maxsuffix[i] = max(maxsuffix[i+1], suffixMaxSum[i])

    maxSum = 0
    for i in range(n+1):
        maxSum = max(maxSum, maxprefix[i], maxsuffix[i+1])

    return maxSum

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Maximum Subarray is:', maxSubarraySum(b))