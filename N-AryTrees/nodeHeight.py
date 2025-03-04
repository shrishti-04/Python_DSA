# Given a tree of N nodes; find the height of each node and print it; the tree is rooted at node 1.

# Basically we will use dp on trees to solve this problem. We will use a dfs to calculate the height of each node.
# We will use a bottom up approach to solve this problem. We will first calculate the height of the children of a node and then calculate the height of the node itself.

def dfs(node, g, visited, parent, height):
    visited[node] = 1

    for x in g[node]:
        if(visited[x] == 0):
            parent[x] = node
            dfs(x, g, visited, parent, height)

    h = 0
    for child in g[node]:
        if(visited[child] == 0):
            continue
        h = max(h, height[child])

    height[node] = 1 + h

n = int(input('enter the number of nodes: '))
g = [[]*(n+1) for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input('Enter the edge: ').split())
    g[x].append(y)
    g[y].append(x)

visited = [0] * (n+1)
parent = [0] * (n+1)
height = [0] * (n+1)

dfs(1, g, visited, parent, height)
print(height[1:])

    