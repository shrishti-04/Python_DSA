# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

def mergeAlternatively(word1, word2):
    result = []
    i, j = 0, 0
    while(i<len(word1) and j<len(word2)):
        result.append(word1[i])
        result.append(word2[j])
        i+=1
        j+=1

    result.append(word1[i:])
    result.append(word2[j:])
    answer = ''.join(result)
    return answer

word1 = "abc"
word2 = "pqr"
print(mergeAlternatively(word1, word2))

# Output: apbqcr