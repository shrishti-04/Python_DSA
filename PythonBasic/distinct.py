# WAP to count the distinct element in array

arr = [1,2,2,3,4,5,5,6,6,7]
n = len(arr)
vis = [False    for i in range(n)]

count = 0

for i in range(n):
    if(vis[arr[i]] == False):
        count+=1
        vis[arr[i]] = True
    
print(count)

# WAP to count the frequency of every elemnt

arr = [1,2,2,3,4,5,5,6,6,7]
n = len(arr)
vis = [False    for i in range(n)]

count = 0

for i in range(n):
    if (vis[arr[i]] == False):
        count=1
        vis[arr[i]] = True
        for j in range(i+1, n):
            if(arr[i] == arr[j]):
                count+=1
                vis[arr[j]] = True
        print(arr[i], '->', count)