# Find the sum of all the surface nodes and also find the maximum.

def maxSumDFS(node, g, visited, parent, sums, b):

    visited[node] = 1

    for x in g[node]:
        if(visited[x] == 0):
            parent[x] = node
            maxSumDFS(x, g, visited, parent, sums, b)

    s = 0
    for child in g[node]:
        if(visited[child] == 0):
            continue
        else:
            s += sums[child]

    sums[node] = b[node] + s

n = int(input('enter the number of nodes: '))
g = [[] for _ in range(n+1)]
b = [0]*(n+1)

i = 1
while(i<n):
    x, y = map(int, input('Enter the edge: ').split())
    g[x].append(y)
    g[y].append(x)
    i+=1

for i in range(1, n+1):
    b[i] = int(input('Enter the value of node: '))

visited = [0]*(n+1)
parent = [0]*(n+1)
sums = [0]*(n+1)
maxSumDFS(1, g, visited, parent, sums, b)

maxSum = 0
for i in range(1, n+1):
    maxSum = max(maxSum, sums[i])

print(maxSum)