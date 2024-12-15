# to find the frequency of the element in array using hashmap.

from collections import defaultdict

n = int(input())
arr = []
hash_arr = defaultdict(int)

for i in range(n):
    num = int(input())
    arr.append(num)
    hash_arr[num] += 1
    
q = int(input())

for i in range(q):
    query = int(input())
    count = hash_arr[query]
    print(count)
    
# Here the time complexity will be reduced than the hash array solution
# that is O(N)
# Because we are just using array as an input
