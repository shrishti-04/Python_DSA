# Find count of number of subarrays with sum ==  k 

# Brute Force Approach

def main():
    n = int(input('Enter the number of array elements: '))
    arr = [0]*(n+1)
    for i in range(1, n+1):
        arr[i] = int(input('Enter your element for array: '))

    k = int(input('Enter a number which should be equal with subarray sum: '))
    count = 0

    for j in range(1, n+1):
        sum_count = 0
        for i in range(j, 0, -1):
            sum_count += arr[i]
            if(sum_count == k):
                count += 1

    print(count)

main()

# Optimized Solution using Hashing

def countSubarrays(arr, k):
    sum = 0
    count = 0
    hash_arr = {}

    hash_arr[0] = 1

    for i in arr:
        sum += i
        if(sum-k in hash_arr):
            count += hash_arr[sum-k]

        hash_arr[sum] = hash_arr.get(sum, 0) + 1

    return count

arr = [5, 1, 3, 8, 3, 6, 1]
k = 4

ans = countSubarrays(arr, k)
print(ans)