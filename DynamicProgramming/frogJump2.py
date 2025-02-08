# Problem Statement
# There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi.

# There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:

# If the frog is currently on Stone i, jump to one of the following: Stone i+1, i+2, …, i+K. 
# Here, a cost of ∣hi − hj∣ is incurred, where j is the stone to land on.

# Find the minimum possible total cost incurred before the frog reaches Stone N.

def frogJump():
    a = []
    n = int(input('Enter the number of stones: '))
    for i in range(n):
        a.append(int(input('Enter the height of stone: ')))

    k = int(input('Enter the maximum number of jumps: '))

    if(n == 1):
        print(0)
        return

    dp = [0] * n
    dp[0] = 0

    if(n > 1):
        dp[1] = abs(a[0] - a[1])

    for i in range(2, n):
        answer = float('inf')
        for j in range(1, k+1):
            if(i-j >= 0):
                option = abs(a[i-j] - a[i]) + dp[i-j]
                answer = min(answer, option)

        dp[i] = answer

    print(dp[n-1])

frogJump()
