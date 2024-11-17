# John Watson knows of an operation called a right circular rotation on an array of integers. 
# One rotation operation moves the last array element to the first position and shifts all remaining elements right one. 
# To test Sherlock's abilities, Watson provides Sherlock with an array of integers. 
# Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

# Example
# a = [3, 4, 5]
# k = 2
# queries = [1, 2]


# Here k is the number of rotations on a, and queries holds the list of indices to report. 
# First we perform the two rotations: [3, 4, 5] -> [5, 3, 4] -> [4, 5, 3]

# Now return the values from the zero-based indices 1 and 2 as indicated in the queries array.

# a[1] = 5
# a[2] = 3

def rotation(a, k, queries):
    k = k%len(a)
    ans = []
    
    for i in range(k):
        rot = a.pop(-1)
        a.insert(0, rot)
    
    for i in queries:
        ans.append(a[i])
        
    return ans

valueRotation = rotation([2, 3, 4, 5], 2, [0, 1, 2, 3])
print(valueRotation)

# another method because above method takes more time complexity i.e. O(K*N)
# better to use this code

def rotation(a, k, queries):
    k = k%len(a)
    num_rotations = a[-k:] + a[:-k]
    
    ans = [num_rotations[i]     for i in queries]
    return ans

valueRotation = rotation([2, 3, 4, 5], 2, [0, 1, 2, 3])
print(valueRotation)