# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, 
# discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, 
# cut that length from each of the longer sticks and then discard all the pieces of that shortest length. 
# When all the remaining sticks are the same length, they cannot be shortened so discard them.

# Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.

# Example
# arr = [1, 2, 3]

# The shortest stick length is 1, so cut that length from the longer two and discard the pieces of length 1. Now the lengths are arr = [1, 2]. 
# Again, the shortest stick is of length 1, so cut that amount from the longer stick and discard those pieces. 
# There is only one stick left, arr = [1], so discard that stick. The number of sticks at each iteration are answer = [3, 2, 1].

# there can be two methods, one can be in short form and another can be in expanded form

# expanded form
def cutStick(arr):
    
    result = []
    while(len(arr) > 0):
        mini = min(arr)
        result.append(len(arr))
    
        new_arr = []
        for i in arr:
            length_cut = i - mini
            if(length_cut > 0):
                new_arr.append(length_cut)

        arr = new_arr
    return result

cutted_sticks = cutStick([5, 4, 4, 2, 2, 8])
print(cutted_sticks)

# short form but easy way

def cuttedStick(arr):
    total = []
    while(len(arr) > 0):
        total.append(len(arr))
        minii = min(arr)
        arr = [j-minii    for j in arr    if j-minii > 0]
        
    return total

cutted = cuttedStick([2, 6, 5, 1, 4, 3])
print(cutted)