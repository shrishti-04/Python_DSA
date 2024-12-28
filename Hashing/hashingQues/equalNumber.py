# Check if there are any two Equal numbers in an array at a distance less than or equal to k

# Brute Force

def nearDis(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if(arr[i] == arr[j] and j-i <= k):
                return True
    return False

def main():
    arr = [1, 1, 3, 1, 2, 3]
    k = 2

    if(nearDis(arr, k)):
        print('Yes')
    else:
        print('No')

main()

# Hashing Method

def neardis(nums, k):
    num_dict = {}

    for i, num in enumerate(nums):
        if(num in num_dict and i - num_dict[num] <= k):
            return True
        num_dict[num] = i
    return False

def main():
    nums = [1, 1, 3, 1, 2, 3]
    k = 2

    if(neardis(nums, k)):
        print('YES')
    else:
        print('NO')

main()
