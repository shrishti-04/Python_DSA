# Search an element in an array

# You are given an array A of size N and an element X. Your task is to find whether the array A 
# contains the element X or not.

# Input Format
# The first line contains two space-separated integers N and X — the size of array and the element to be searched. 
# The second line contains all the elements of array 

# A Output Format
# Output "YES" if the element X is present in A, otherwise output "NO".

# Sample Input 1
# 5 2
# 1 2 3 4 5
# Sample Output 1
# YES

n, x = map(int, input().split())
array = list(map(int, input().split()))

if(x in array):
    print("YES")
else:
    print("NO")