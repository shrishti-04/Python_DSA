# Paypal OA :-> Find the largest valid substring - Valid string is a string where adjacent pair of char have diff<=k

def main():
    n = int(input('Enter the length of the string: '))
    s = []
    for i in range(n):
        s.append(input('Enter the character: '))

    k = int(input('Enter the maximum difference between adjacent characters: '))

    dp = [0] * n
    dp[0] = 1

    max_len = 1
    max_index = 0

    for i in range(1, n):
        if(abs(ord(s[i])-ord(s[i-1])) <= k):
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1

        if(dp[i] >= max_len):
            max_len = dp[i]
            max_index = i

    start_index = max_index - max_len + 1
    print(s[start_index:start_index + max_len])

main()

# Output:

# Enter the length of the string: 10

# Enter the character: a
# Enter the character: b
# Enter the character: a
# Enter the character: a
# Enter the character: b
# Enter the character: c
# Enter the character: a
# Enter the character: d
# Enter the character: e
# Enter the character: f

# Enter the maximum difference between adjacent characters: 2

# ['a', 'b', 'a', 'a', 'b', 'c', 'a']