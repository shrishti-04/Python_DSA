# Find First and Last Position of Element in Sorted Array.

def searchRange(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ans = [-1, -1]

    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] == target):
            ans[0] = mid
            high = mid - 1
        elif(target <= nums[mid]):
            high = mid - 1
        else:
            low = mid + 1

    low = 0
    high = n - 1
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] == target):
            ans[1] = mid
            low = mid + 1
        elif(target <= nums[mid]):
            high = mid - 1
        else:
            low = mid + 1

    return ans

nums = [5, 7, 7, 8, 8, 10]
target = 7
print(searchRange(nums, target))

# Output: [1, 2]