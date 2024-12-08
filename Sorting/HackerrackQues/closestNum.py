# Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, 
# but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have 
# the smallest absolute difference between them.

# Example
# arr = [5, 2, 3, 4, 1]

# Sorted, arr = [1, 2, 3, 4, 5]. Several pairs have the minimum difference of 1: [(1, 2), (2, 3), (3, 4), (4, 5)]. 
# Return the array [1, 2, 2, 3, 3, 4, 4, 5].

# Note
# As shown in the example, pairs may overlap.

# Given a list of unsorted integers, arr, find the pair of elements that have the smallest 
# absolute difference between them. If there are multiple pairs, find them all.

def closestNum(arr):
    arr.sort()
    min_diff = float('inf')
    pairs = []

    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if(diff < min_diff):
            min_diff = diff
            pairs = [(arr[i], arr[i+1])]
        elif(diff == min_diff):
            pairs.append((arr[i], arr[i+1]))

    result = []
    for pair in pairs:
        result.extend(pair)

    return result

ans = closestNum([4, 5, 2, 3, 1])
print(ans)
