# For each node in the graph find if its reachable or not from the source node.

from collections import deque

n, m = map(int, input('Enter the number of nodes and edges: ').split())
graph = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input('Enter the edge: ').split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
source = int(input('Enter the source node: '))
q.append(source)
visited = [0]*(n+1)
visited[source] = 1
level = [0]*(n+1)
level[source] = 0

while q:
    x = q.popleft()
    for y in graph[x]:
        if(visited[y] == 0):
            q.append(y)
            visited[y] = 1
            level[y] = level[x] + 1

while(i<=n):
    if(visited[i] == 0):
        print('you cannot reach node', i, 'from source node', source)
    else:
        print('you can reach node', i, 'from source node', source)
    i += 1