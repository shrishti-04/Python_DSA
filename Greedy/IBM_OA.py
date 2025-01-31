# Given an array of size N; and a target 
# -> find the minimum number of operations needed to make all elements of array equal to target 
# -> there are multiple target in order of Q

# Brute force:

def minOperations(arr, target):

    q = int(input('Enter the number of targets: '))

    for i in range(q):
        target = int(input('Enter your target: '))
        operations = 0

        for j in range(n):
            operations += abs(arr[j] - target)

    print(operations)

n = int(input('Enter the number of elements in arr: '))
arr = []

for i in range(n):
    arr.append(int(input('Enter arr elements: ')))

target = int(input('Enter your target: '))
print(minOperations(arr, target))

# Greedy approach

def binarySearch(target):
    low = 0
    high = len(arr)

    while(low < high):
        mid = (low + high) // 2
        if(target >= arr[mid]):
            low = mid + 1
        else:
            high = mid

    return low-1

def minOperations():
    global arr
    n = int(input('Enter number of ele in arr: '))
    total_sum = 0
    arr = []
    for i in range(n):
        arr.append(int(input('Enter elements: ')))
    arr.sort()

    # prefix sum
    prefix_sum = [0] * (n+1)
    total_sum = sum(arr)

    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

    q = int(input('Enter the number of targets: '))
    for _ in range(q):
        target = int(input('Enter your target: '))
        index = binarySearch(target)

        left_operations = target * index - (prefix_sum[index])
        right_operations = (total_sum - prefix_sum[index]) - (target * (n - index))

    return (left_operations + right_operations)

print(minOperations())



