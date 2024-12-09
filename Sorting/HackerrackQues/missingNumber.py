# Given two arrays of integers, find which elements in the second array are missing from the first array.

# Example
# arr = [7, 2, 5, 3, 5, 3]
# brr = [7, 2, 5, 4, 6, 3, 5, 3]

# The brr array is the orginal list. The numbers missing are [4, 6].

def missingNum(arr, brr):
    for i in arr:
        if(i in brr):
            brr.remove(i)

    return sorted(list(set(brr)))

result = missingNum([7, 2, 5, 3, 5, 3], [7, 2, 5, 4, 6, 3, 5, 3])
print(result)