# Find count of number of subarrays with sum ==  k 

def countSubarrays(arr, k):
    sum = 0
    count = 0
    hash_arr = {}

    hash_arr[0] = 1

    for i in arr:
        sum += i
        if(sum-k in hash_arr):
            count += hash_arr[sum-k]
        if(sum in hash_arr):
            hash_arr[sum] += 1
        else:
            hash_arr[sum] = 1

    return count

arr = [3, 4, 5, 1, 3, 7]
k = 6

ans = countSubarrays(arr, k)
print(ans)