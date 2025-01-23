# Find the largest valid substring - Valid string is a string where any pair of characters have diff <= k

def largestValidSubstring(s, k):
    n = len(s)
    i = 0
    max_len = 0

    for j in range(i, n):
        g = {}
        if(s[j] in g):
            g[s[j]] += 1
        else:
            g[s[j]] = 1

        max_ele = max(g.keys())
        min_ele = min(g.keys())

        d = ord(max_ele) - ord(min_ele)

        while(d > k):
            g[s[i]] -= 1
            if(g[s[i]] == 0):
                del g[s[i]]

            i += 1
            max_ele = max(g.keys())
            min_ele = min(g.keys())

            d = ord(max_ele) - ord(min_ele)
            

        max_len = max(max_len, (j-i+1))

    return max_len

print(largestValidSubstring("abaccc", 2)) # 6