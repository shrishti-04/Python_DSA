# We are given an Array of Numbers. We have to find and print any Number with Maximum Frequency and Minimum Frequency.

# Example Testcase:-

# Arr = [3, 2, 3, 2, 4, 3]

# Frequencies of Elements of Array are:-

# 3 - 3
# 2 - 2
# 4 - 1

# Maximum Frequency:- Element is 3, Frequency is 3
# Minimum Frequency:- Element is 4, Frequency is 1

n = int(input('Enter array length: '))
arr = []
hash_arr = {}
maxiFreq = float('-inf')
maxiEle = 0
miniFreq = float('inf')
miniEle = 0

for i in range(n):
    num = int(input('Enter your element: '))
    arr.append(num)
    hash_arr[num] = hash_arr.get(num, 0) + 1

for num, freq in hash_arr.items():
    if(freq >= maxiFreq):
        maxiFreq = freq
        maxiEle = num

    elif(freq <= miniFreq):
        miniFreq = freq
        miniEle = num

print("Max frequency element: " + str(maxiEle) + " with frequency: " + str(maxiFreq))
print("Min frequency element: " + str(miniEle) + " with frequency: " + str(miniFreq))