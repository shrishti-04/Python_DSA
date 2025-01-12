# Find largest/smallest subarray with sum k in Given Array

# Brute force approach

# def subarraySumMaxLen(arr, k):
#     n = len(arr)
#     max_len = 0
#     min_len = float('inf')

#     for i in range(n):
#         summ = 0
#         for j in range(i, n):
#             summ += arr[j]
#             if(summ == k and max_len < j-i+1):
#                 max_len = j-i+1
#             if(summ == k and min_len > j-i+1):
#                 min_len = j-i+1

#     print("Max Length: ", max_len)
#     print("Min Length: ", min_len)

# answer = subarraySumMaxLen([1, 4, 10, 3, 1, 2, 2, 1], 5)
# print(answer)

# Optimised approach using hashmap

def subarraySumLen(arr, k):
    n = len(arr)
    prefix_arr ={0:0}
    prefix_arr2 = {0:0}
    max_lex = 0
    min_len = float('inf')
    prefix_sum = 0
    result = (-1, -1)


    for j in range(n):
        prefix_sum += arr[j]

        x = prefix_sum - k
        if(x in prefix_arr and x in prefix_arr2):
            length = j - prefix_arr[x] + 1
            length2 = j - prefix_arr2[x] + 1

            if(max_lex < length):
                max_len = length
                result = (prefix_arr[x], j)
            
            if(min_len > length):
                min_len = length
                result2 = (prefix_arr2[x], j)

        if(prefix_sum not in prefix_arr and prefix_sum not in prefix_arr2):
            prefix_arr[prefix_sum] = j
            prefix_arr2[prefix_sum] = j

    return result, result2

arr = [1, 4, 10, 3, 1, 2, 2, 1]
k = 5

answer1, answer2 = subarraySumLen(arr, k)
if(answer1 != (-1, -1) and answer2 != (-1, -1)):
    print(f"Largest subarray with sum {k} is from index {answer1[0]} to {answer1[1]}")
    print(f"Smallest subarray with sum {k} is from index {answer2[0]} to {answer2[1]}")
else:
    print(f"No subarray with sum {k}")

# Output:
# Largest subarray with sum 5 is from index 4 to 7
# Smallest subarray with sum 5 is from index 0 to 1
