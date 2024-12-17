# Check if there are any two Equal numbers in an array at a distance less than or equal to k

def contains_nearby_duplicate_optimized(nums, k):
    num_indices = {}

    for i, num in enumerate(nums):
        if(num in num_indices and i-num_indices[num] <= k):
            return True
        num_indices[num] = i
    return False

def main():
    nums = [1, 1, 3, 1, 2, 3]
    k = 2

    if(contains_nearby_duplicate_optimized(nums, k)):
        print("There are two equal numbers within distance", k)
    else:
        print("No two equal numbers found within distance", k)

main()
