# Problem Statement
# There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi.

# There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:

# If the frog is currently on Stone i, jump to Stone i+1 or Stone i+2. Here, a cost of ∣hi − hj∣ is incurred, where j is the stone to land on.
# Find the minimum possible total cost incurred before the frog reaches Stone N.

def frogJump():
    a = []
    n = int(input('Enter the number of stones: '))
    for i in range(n):
        a.append(int(input('Enter the height of stone: ')))

    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(a[0] - a[1])

    for i in range(2, n):
        dp[i] = min(abs(a[i-1] - a[i]) + dp[i-1], abs(a[i-2] - a[i]) + dp[i-2])

    print(dp[n-1])

frogJump()