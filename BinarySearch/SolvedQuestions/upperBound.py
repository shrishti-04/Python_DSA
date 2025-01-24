# -> Given a sorted array of size “N”; find the index of the number in the array 
# which is just greater than x and as close as possible to x.

# -> Upper Bound (x) = Returns index of the number which is just greater than x and as close as possible to x.

def upperBound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = -1

    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] > target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

arr = [1, 2, 2, 3, 4, 6]
target = 2
print(upperBound(arr, target))