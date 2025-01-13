# LeetCode Question: https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Brute force approach

def anagram(s, t):
    s = sorted(s)
    t = sorted(t)

    return s == t

ans = anagram("anagram", "nagaram")
print(ans)

# Optimised approach 1 using hashmap

from collections import defaultdict

def anagram(s, t):
    if(len(s) != len(t)):
        return False
    
    a = defaultdict(int)
    b = defaultdict(int)
    n = len(s)

    for i in range(n):
        a[s[i]] += 1
        b[t[i]] += 1

    for c in range(ord('a'), ord('z') + 1):
        if(a[chr(c)] != b[chr(c)]):
            return False
        
    return True

ans = anagram("pasy", "casy")
print(ans)

# Optimised Approach 2 using hashmap using reduce function

from collections import defaultdict

def anagrams(s, t):
    if(len(s) != len(t)):
        return False
    
    counts = defaultdict(int)

    for i in range(len(s)):
        counts[s[i]] += 1
        counts[t[i]] -= 1

    for count in counts.values():
        if(count != 0):
            return False
        
    return True

ans = anagrams("anagram", "nagaram")
print(ans)