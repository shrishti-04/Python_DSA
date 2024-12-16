# to find the frequency of the element in array using hashing

n = int(input('enter length of arr: '))
arr = []
hash_arr = [0]*100

for i in range(n):
    num = int(input('Enter a number: '))
    arr.append(num)
    hash_arr[num] += 1

q = int(input('No. of queries: '))

for j in range(q):
    element = int(input('Enter no. in query: '))
    count = hash_arr[element]
    print(count)
    
# Here the time complexity will be reduced than the brute force solution
# that is O(N + Q)
# Addition is always better than the multiplication as it takes less time in time complexity