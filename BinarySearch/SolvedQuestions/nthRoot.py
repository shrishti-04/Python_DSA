# Given two numbers N and A, find N-th root of A. In mathematics, 
# Nth root of a number A is a real number that gives A, when we raise it to integer power N. 
# These roots are used in Number Theory and other advanced branches of mathematics.

def func(mid, n, m):
    ans = 1
    for i in range(n):
        ans *= mid
        if(ans > m):
            return 2
    if(ans == m):
        return 1
    return 0

def nthRoot(n, m):
    low = 1
    high = m
    while(low <= high):
        mid = (low + high) // 2
        midn = func(mid, n, m)
        if(midn == 1):
            return mid
        elif(midn == 2):
            high = mid - 1
        else:
            low = mid + 1
    return -1

n = 4
m = 81
print(nthRoot(n, m)) # Output: 3
