# Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once.

# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

def singleUniqueElement(arr, target):
    n = len(arr)
    low = 0
    high = n-1

    while(low < high):
        mid = (low + high) // 2

        if(mid % 2 == 0):
            if(arr[mid] == arr[mid + 1]):
                low = mid + 2
            else:
                high = mid
        
        else:
            if(arr[mid] == arr[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1

    return arr[low]

arr = [1, 1, 2, 2, 3, 3, 4, 8, 8]
target = 2
print(singleUniqueElement(arr, target))