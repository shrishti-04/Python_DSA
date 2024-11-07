# to find the frequency of the element in array.

arr = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
n = len(arr)
vis = [False    for i in range(n)]
# O(N)
count = 0

for i in range(n):
    # O(N) again
    if(vis[arr[i]] == False):
        count = 1
        vis[arr[i]] = True
        for j in range(i+1, n):
            # O(n)
            if(arr[i] == arr[j]):
                count += 1
                vis[arr[j]] = True
        
        print(arr[i], '->', count)
        
# Here time complexity will be
# O(N^3)
