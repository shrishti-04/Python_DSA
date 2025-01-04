# # Count all i,j pairs where i<j and abs(b[i]-b[j]) = k [k>=0] 

# # Brute Force

def absDiffCount(arr, k):

    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if(abs(arr[i] - arr[j]) == k):
                count += 1
    return count

def main():
    arr = [1, 7, 5, 9, 2, 12, 3]
    k = 2

    count = absDiffCount(arr, k)
    print("Number of pairs are: ",count)

main()

# Optimised code- Hashing

def absDiffCountPairs(arr, k):
    count = 0
    hash_array = {}

    for j in range(len(arr)):
        if((arr[j] - k) in hash_array):
            count += hash_array[arr[j] - k]
        if((arr[j] + k) in hash_array):
            count += hash_array[arr[j] + k]

        if(arr[j] in hash_array):
            hash_array[arr[j]] += 1
        else:
            hash_array[arr[j]] = 1

    return count

def main():
    arr = [1, 7, 5, 9, 2, 12, 3]
    k = 2
    count = absDiffCountPairs(arr, k)
    print(count)

main()