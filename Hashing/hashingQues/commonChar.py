# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
# You may return the answer in any order.

# Leetcode Question 1002. Find Common Characters

def commonChars(words):
    common_count = [float('inf')] * 26

    for word in words:
        word_count = [0] * 26
        for char in word:
            word_count[ord(char) - ord('a')] += 1

        for i in range(26):
            common_count[i] = min(common_count[i], word_count[i])

    result = []
    for i in range(26):
        result.extend([chr(i + ord('a'))] * common_count[i])

    return result

words = ["bella", "label", "roller"]
print(commonChars(words))