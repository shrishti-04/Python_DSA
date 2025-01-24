# Find an element in the given sorted array using binary search.

def binarySearch(arr, target):

    n = len(arr)
    low = 0
    high = n - 1

    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] == target):
            return mid
        elif(target <= arr[mid]):
            high = mid - 1
        else:
            low = mid + 1

    return -1

arr = [1, 2, 2, 3, 4, 6]
target = 2
print(binarySearch(arr, target))

        