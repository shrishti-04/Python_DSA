# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. 
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# Example
# arr = [1, 1, 2, 2, 3]

# There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

# Function Description

# Complete the migratoryBirds function in the editor below.

# migratoryBirds has the following parameter(s):

# int arr[n]: the types of birds sighted

def migratoryBirds(arr):
    storage = {1:0, 2:0, 3:0, 4:0, 5:0}
    ans = 0
    max_count = 0
    
    for i in range(len(arr)):
        storage[arr[i]] += 1
        
    for i_type, count in storage.items():
        if(count > max_count):
            max_count = count
            ans = i_type
            
    print(ans)
    
migratoryBirds([1, 4, 4, 4, 5, 3])
            