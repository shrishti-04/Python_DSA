def charFreq(char, s):
    count = 0
    for i in range(len(s)):
        if(s[i] == char):
            count += 1

    return count

ans = charFreq('s', 'shrishti')
print(ans)