# Find Sum of Range  [l……….r] where(l<=r) using Prefix sum. 

def calcPrefixSum(arr):
    hash_arr = {}
    sum_arr = 0

    for i in range(len(arr)):
        sum_arr += arr[i]
        hash_arr[i] = sum_arr

    return hash_arr

def rangeSum(l, r, hash_arr):
    if(l == 0):
        return hash_arr[r]
    else:
        return hash_arr[r] - hash_arr[l-1]
    
def main():
    arr = [3, 6, 5, 4, 8, 1]
    prefix_hash = calcPrefixSum(arr)
    l = 2
    r = 5
    result = rangeSum(l, r, prefix_hash)
    print(result)

main()