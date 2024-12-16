# to find the frequency of the element in array using hashmap.

n = int(input('enter length of arr: '))
arr = []
hash_arr = {}

for i in range(n):
    num = int(input('Enter a number: '))
    arr.append(num)
    if(num in hash_arr):
        hash_arr[num] += 1
    else:
        hash_arr[num] = 1

q = int(input('No. of queries: '))

for j in range(q):
    element = int(input('Enter no. in query: '))
    count = hash_arr.get(element, 0)
    print(element, '->', count)
    
# Here the time complexity will be reduced than the hash array solution
# that is O(N)
# Because we are just using array as an input
