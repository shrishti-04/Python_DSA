# We are given ‘2’ arrays . Select some elements from both of these arrays (select a subset) such that:-

# --->1. Sum of those elements is maximum(Sum of the subset is maximum).
# --->2. No 2 elements in the subset should be consecutive.(Note:-If you select, say the 5th element from Array-1, then you are not allowed to select 4th element from either Array-1 or Array-2 nor are you allowed to select the 5th element from Array -2 all of them are considered consecutive :-) )


# Example:->
# Array 1(a1) : {1,5,3,21234}
# Array 2(a2) : {-4509,200,3,40}

# Answer:- (200+21234=21434)

def maxTwoArrSumNonAdj():
    n = int(input('Enter the length of arrays: '))

    a = [0]*n
    b = [0]*n

    for i in range(n):
        a[i] = int(input('Enter a array element: '))

    for i in range(n):
        b[i] = int(input('Enter b array element: '))

    dp = [0]*n
    dp[0] = max(a[0], b[0])
    dp[1] = max(dp[0], max(a[1], b[1]))

    for i in range(2, n):
        dp[i] = max(dp[i-1], a[i] + dp[i-2], b[i] + dp[i-2])

    print(dp[n-1])

maxTwoArrSumNonAdj()
