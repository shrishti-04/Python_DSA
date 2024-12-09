# arr = [1, 1, 3, 2, 1]
# All of the values are in the range [0...3], so create an array of zeros, result = [0, 0, 0, 0]. The results of each iteration follow:

# i	arr[i]	result
# 0	1	[0, 1, 0, 0]
# 1	1	[0, 2, 0, 0]
# 2	3	[0, 2, 0, 1]
# 3	2	[0, 2, 1, 1]
# 4	1	[0, 3, 1, 1]
# The frequency array is [0, 3, 1, 1]. These values can be used to create the sorted array as well: sorted = [1, 1, 1, 2, 3].

def countingSort(arr):
    result = [0] * 100
    for i in arr:
        result[i] += 1
    return result

ans = countingSort([1, 1, 3, 2, 1])
print(ans)