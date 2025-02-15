# DFS is a depth first search algorithm that traverses a graph in a depthward motion 
# and uses a stack to keep track of the nodes that it has visited.

from collections import deque

n, m = map(int, input('Enter the number of nodes and edges: ').split())
g = [[] for i in range(n+5)]

for i in range(m):
    x, y = map(int, input('Enter the edge: ').split())
    g[x].append(y)
    g[y].append(x)

source = int(input('Enter the source node: '))
visited = [0]*(n+1)
parent = [0]*(n+1)

def dfs(node, g, visited, parent):
    print(node, end=' ')
    visited[node] = 1
    for x in g[node]:
        if(visited[x] == 0):
            parent[x] = node
            dfs(x, g, visited, parent)

dfs(source, g, visited, parent)

# Output:

# Enter the number of nodes and edges: 8 7
# Enter the edge: 1 2
# Enter the edge: 1 3
# Enter the edge: 2 4
# Enter the edge: 2 5
# Enter the edge: 4 8
# Enter the edge: 3 6
# Enter the edge: 3 7
# Enter the source node: 1

# 1 2 4 8 5 3 6 7