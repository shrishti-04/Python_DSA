# to find the frequency of the element in array using hashing

n = int(input())
array = []
hash_array = [0] * 51

for i in range(n):
    array.append(int(input()))
    hash_array[array[i]] += 1
    
q = int(input())

for j in range(q):
    query = int(input())
    count = hash_array[query]
    print(count)
    
# Here the time complexity will be reduced than the brute force solution
# that is O(N + Q)
# Addition is always better than the multiplication as it takes less time in time complexity