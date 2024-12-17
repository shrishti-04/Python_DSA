# Count all the (i,j) Pairs such that b[i] + b[j] == k (count of such pairs.) [i<j]

# Brute Force

# def countPairs(arr, k):
#     count = 0
#     for i in range(len(arr) - 1):
#         for j in range(i+1, len(arr)):
#             if(arr[i] + arr[j] == k):
#                 count += 1
#     return count

# ans = countPairs([1, 2, 5, 7, 4], 6)
# print(ans)

# hashing

def countPairs(arr, k):
    count = 0
    pairs = {}

    for i in arr:
        ele = k - i
        if(ele in pairs):
            count += 1
        pairs[i] = True

    return count

ans = countPairs([1, 2, 5, 7, 4], 6)
print(ans)