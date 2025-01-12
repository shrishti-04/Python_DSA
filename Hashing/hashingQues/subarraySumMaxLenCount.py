# Find count of shortest/largest subarrays with sum k in given array

# Brute force approach

def subarraySumMaxLenCount(arr, k):
    n = len(arr)
    max_len = 0
    min_len = float('inf')
    max_count = 0
    min_count = 0
    summ = 0

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]
            if(summ == k):
                length = j-i+1
                if(max_len < length):
                    max_len = length
                    max_count = 1
            
                elif(max_len == length):
                    max_count += 1

                if(min_len > length):
                    min_len = length
                    min_count = 1
                
                elif(min_len == j-i+1):
                    min_count += 1

    print(max_count)
    print(min_count)
    return max_count, min_count

answer = subarraySumMaxLenCount([1, 2, 3, 4, 2, 5], 5)
print(answer)

# Optimised approach using hashmap

def subarraySumMaxLenCount(arr, k):
    n = len(arr)
    prefix_arr = {0:-1}
    prefix_arr2 = {0:-1}
    max_len = 0
    min_len = float('inf')
    max_count = 0
    min_count = 0
    prefix_sum = 0

    for j in range(n):
        prefix_sum += arr[j]

        x = prefix_sum - k
        if(x in prefix_arr and x in prefix_arr2):
            length = j - prefix_arr[x] + 1
            length2 = j - prefix_arr2[x] + 1
            if(max_len < length):
                max_len = length
                max_count = 1

            elif(max_len == length):
                max_count += 1

            if(min_len > length2):
                min_len = length2
                min_count = 1

            elif(min_len == length2):
                min_count += 1

        if(prefix_sum not in prefix_arr and prefix_sum not in prefix_arr2):
            prefix_arr[prefix_sum] = j
            prefix_arr2[prefix_sum] = j

    print('Max Length: ', max_len, 'with Max Count: ', max_count)
    print('Min Length: ', min_len, 'with Min Count: ', min_count)

answer = subarraySumMaxLenCount([1, 2, 3, 4, 2, 5], 5)
print(answer)