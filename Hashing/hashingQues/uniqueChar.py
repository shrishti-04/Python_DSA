# Leetcode Question 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

def firstUniqueChar(s):
    freq = dict()

    for char in s:
        freq[i] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if(freq[char] == 1):
            return i
        
    return -1

s = "shrishti"
print(firstUniqueChar(s))
