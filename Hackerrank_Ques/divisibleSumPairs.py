# Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i < j and ar[i] + ar[j] is divisible by k.

# Example
# ar = [1, 2, 3, 4, 5, 6]
# k = 5

# Three pairs meet the criteria: [1, 4], [2, 3], [4, 6].

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if((ar[i] + ar[j]) % k == 0):
                count += 1
                
    print(count)
    
divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6])