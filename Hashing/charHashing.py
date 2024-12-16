# This is for string

def stringHasing(s):
    s = input('Enter a string: ')
    hash_arr = [0]*26

    for i in s:
        hash_arr[ord(i) - ord('a')] += 1

    q = int(input('no. of queries: '))

    for j in range(q):
        char = input('single character: ')
        print(hash_arr[ord(char) - ord('a')])

stringHasing('shrishti')

# output

# Enter a string: shrishti
# no. of queries: 4
# single character: s
# 2
# single character: z
# 0
# single character: r
# 1
# single character: i
# 2