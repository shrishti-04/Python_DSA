# Problem
# Given n, i.e. total number of nodes in an undirected graph numbered from 1 to n and an integer e, i.e. 
# total number of edges in the graph. Find the shortest distance of all the node from the source node s.

# Input Format:

# First line of input line contains two integers n and e. Next e line will contain two integers u and v 
# meaning that node u and node v are connected to each other in undirected fashion. Last line will contain an integer s denoting the source node.

# Output Format:

# For each input graph print the shortest distance of each node from the source node.

from collections import deque

n, m = map(int, input().split())
g =[[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

source = int(input('Enter source node: '))
q = deque()
q.append(source)

visited = [0] * (n+1)
visited[source] = 1
level = [0] * (n+1)
level[source] = 0

while q:
    x = q.popleft()
    for y in g[x]:
        if(visited[y] == 0):
            q.append(y)
            visited[y] = 1
            level[y] = level[x] + 1

i = 1
while(i <= n):
    print(level[i], end=' ')
    i += 1