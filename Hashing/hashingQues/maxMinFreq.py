# We are given an Array of Numbers. We have to find and print any Number with Maximum Frequency and Minimum Frequency.

# Example Testcase:-

# Arr = [3, 2, 3, 2, 4, 3]

# Frequencies of Elements of Array are:-

# 3 - 3
# 2 - 2
# 4 - 1

# Maximum Frequency:- Element is 3, Frequency is 3
# Minimum Frequency:- Element is 4, Frequency is 1

# Brute Force

# def minMaxFreq(arr):
#     n = len(arr)
#     min_count = float('inf')
#     max_count = 0
#     min_ele = None
#     max_ele = None

#     for i in range(n):
#         count = 0
#         for j in range(i, n):
#             if(arr[i] == arr[j]):
#                 count += 1

#         if(count < min_count):
#             min_count = count
#             min_ele = arr[i]

#         if(count > max_count):
#             max_count = count
#             max_ele = arr[i]

#     print('Minimum Frequency: ', min_count, 'whose element is: ', min_ele)
#     print('Maximum Frequency: ', max_count, 'whose element is: ', max_ele)

# minMaxFreq([5, 3, 3, 3, 1, 1])

# Hashing Method

def minMaxFreq(arr):

    hash_arr = {}
    min_count = float('inf')
    max_count = float('-inf')
    min_ele = 0
    max_ele = 0

    for i in arr:
        hash_arr[i] = hash_arr.get(i, 0) + 1

    for i, count in hash_arr.items():
        if(count < min_count):
            min_count = count
            min_ele = i

        if(count > max_count):
            max_count = count
            max_ele = i

    print('Minimum Frequency: ', min_count, 'whose element is: ', min_ele)
    print('Maximum Frequency: ', max_count, 'whose element is: ', max_ele)

minMaxFreq([1, 3, 3, 3, 5, 1])