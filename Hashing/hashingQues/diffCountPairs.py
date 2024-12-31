# Count All ((i,j) pairs such that b[i] - b[j] == k (count of such pairs.) [i<j]
           
# Brute Force

def diffCountPairs(arr, k):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if(arr[i]-arr[j] == k):
                count += 1

    return count

def main():
    arr = [6, 4, 3, 8, 1, 1, 7, 9]
    k = 2

    count = diffCountPairs(arr, k)
    print(count)

main()

# Hashing Method

def diffCountPairs(arr, k):
    count = 0
    hash_arr = {}

    for i in arr:
        value = k + i
        if(value in hash_arr):
            count += 1
        hash_arr[i] = True

    return count

def main():
    arr = [6, 4, 3, 8, 1, 1, 7, 9]
    k = 1

    count = diffCountPairs(arr, k)
    print(count)

main()