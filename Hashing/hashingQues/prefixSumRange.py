# Find Sum of Range  [l……….r] where(l<=r) using Prefix sum.

# Brute Force approach

def prefixSum(arr, l, r):
    sums = 0

    for i in range(l, r+1):
        sums += arr[i]

    return sums

def main():
    arr = [6, 3, 5, 2, 4, 1, 2]
    l = 1
    r = 5

    sums = prefixSum(arr, l, r)
    print(sums)

main()

# Optimized code: Hashing

# to update prefix array use: prefix_array[i] = prefix_arr[i-1] + array[i],
# here array[i] is the current value in normal given array and 
# prefix_arr[i] is value of prefix array which you have created using length of normal array

# to optimise sum we used formulae: prefix_arr[r] - prefix[l-1] to remove all item before l
# and we can correctly get sum of given limits

def prefixArray(arr):
    n = len(arr)
    prefix_array = [0] * n

    for i in range(1, n):
        prefix_array[i] = prefix_array[i-1] + arr[i]

    return prefix_array

def optimisedSum(prefix_array, l, r):
    return prefix_array[r] - prefix_array[l-1]

def main():
    arr = [6, 3, 5, 2, 4, 1, 2]
    l = 1
    r = 5
    prefix_array = prefixArray(arr)

    optiSum = optimisedSum(prefix_array, l, r)
    print(optiSum)

main()