# Number of shortest paths from the source node to all other nodes in the graph.

from collections import deque

n, m = map(int, input('Enter the number of nodes and edges: ').split())
graph = [[] for i in range(n+5)]

for i in range(m):
    x, y = map(int, input('Enter the edge: ').split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
source = int(input('Enter the source node: '))
q.append(source)
visited = [0]*(n+5)
visited[source] = 1
level = [0]*(n+5)
level[source] = 0
ways = [0]*(n+5)
ways[source] = 1

while q:
    x = q.popleft()
    print(x, ways[x])
    for y in graph[x]:
        if(visited[y] == 0):
            q.append(y)
            visited[y] = 1
            level[y] = level[x] + 1
            ways[y] = ways[x] + ways[y]
        else:
            if(level[y] == level[x] + 1):
                ways[y] = ways[x] + ways[y]