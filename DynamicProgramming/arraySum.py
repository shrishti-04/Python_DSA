# We are given an array of integers(a[n]) . We are given multiple queries of the form : (1, i) 
# which means we need to output the sum of all numbers from index- ‘1’ to index ‘i’ of the array.

# Brute Force

# def sumArray(arr):
#     n = len(arr)
#     sums = 0

#     for i in range(n):
#         for j in range(i):
#             sums += arr[i]

#     return sums

# arr = [2, 3, 2, 2, 1, 1, 2]
# ans = sumArray(arr)
# print(ans)

# Optimised Approach: Dynamic Programming

def sumArray(arr):
    n = 5
    dp = [0]*(n+1)
    i = 0

    while(i <= n-1):
        if(i == 0):
            dp[i] = arr[i]
        else:
            dp[i] = dp[i-1] + arr[i]
        i += 1

    q = int(input('Enter queries: '))
    w = [0, 3, 1, 2]
    i = 0

    while(i <= q-1):
        query = w[i]
        print(dp[query])
        i += 1

arr = [2, 3, 2, 2, 1, 1, 2]
sumArray(arr)
