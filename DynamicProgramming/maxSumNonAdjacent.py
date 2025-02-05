# Given an array of integers(positive as well as negative) ,select some elements from this array(select a subset) such that:-

# 1. Sum of those elements is maximum(Sum of the subset is maximum) .
# 2. No two elements in the subset should be consecutive.

# Example :- {2,4,6,7,8}
# Answer:- {2+6+8=16}

def maxSumNonAdjacent():
    n = int(input('Enter the number of array: '))
    arr = [0]*(n)

    for i in range(n):
        arr[i] = int(input('Enter Elements: '))

    dp = [0] * (n)
    l = 0
    dp[0] = max(arr[0], 0)
    dp[1] = max(arr[0], max(arr[1], l))

    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])

    print(dp[n-1])

maxSumNonAdjacent()
