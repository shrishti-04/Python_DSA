# Count all the (i,j) Pairs such that b[i] + b[j] == k (count of such pairs.) [i<j]

# Brute Force

# def countPairs(arr, k):
#     n = len(arr)
#     count = 0

#     for i in range(n):
#         for j in range(i+1, n):
#             if(arr[i] + arr[j] == k and arr[i]<arr[j]):
#                 count += 1
#     return count

# ans = countPairs([2, 6, 3, 9, 1, 4, 7], 5)
# print(ans)

# hashing

def sumpairs(arr, k):
    count = 0
    hash_arr = {}

    for i in arr:
        comp = k - i
        if(comp in hash_arr):
            count += 1
        hash_arr[i] = True

    return count

def main():
    arr = [3, 4, 7, 5, 2, 8, 1]
    k = 5

    count = sumpairs(arr, k)
    print(count)

main()