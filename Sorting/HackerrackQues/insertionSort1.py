# Sorting
# One common task for computers is to sort data. For example, people might want to see all their files 
# on a computer sorted by size. Since sorting is a simple problem with many different possible solutions, 
# it is often used to introduce the study of algorithms.

# Insertion Sort
# These challenges will cover Insertion Sort, a simple and intuitive sorting algorithm. 
# We will first start with a nearly sorted list.

# Insert element into sorted list
# Given a sorted list with an unsorted number  in the rightmost cell, 
# can you write some simple code to insert e into the array so that it remains sorted?

# Since this is a learning exercise, it won't be the most efficient way of performing the insertion. 
# It will instead demonstrate the brute-force method in detail.

# Assume you are given the array arr = [1, 2, 4, 5, 3] indexed 0...4. Store the value of arr[4]. 
# Now test lower index values successively from 3 to 0 until you reach a value that is lower than arr[4], at arr[1] in this case. 
# Each time your test fails, copy the value at the lower index to the current index and print your array. 
# When the next lower indexed value is smaller than arr[4], insert the stored value at the current index and print the entire array.

def insertionSort1(arr):
    n = len(arr)
    key = arr[-1]
    i = n-2

    while(i>=0 and (arr[i] > key)):
        arr[i+1] = arr[i]
        print(*arr)
        i-=1

    arr[i+1] = key
    print(*arr)

insertionSort1([1, 2, 4, 5, 3])