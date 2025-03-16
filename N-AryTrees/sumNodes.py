#  Given a tree of N nodes; rooted at node 1; find the sum of the each subtree in the given tree.

def dfsSum(node, g, visited, parent, sums, b):
    visited[node] = 1

    for x in g[node]:
        if(visited[x] == 0):
            parent[x] = node
            dfsSum(x, g, visited, parent, sums, b)

    s = 0
    for child in g[node]:
        if(visited[child] == 0):
            continue
        else:
            s += sums[child]

    sums[node] = b[node] + s 

n = int(input('enter the number of nodes: '))
g = [[] for _ in range(n+1)]
b = [0] * (n+1)

for i in range(n-1):
    x, y = map(int, input('Enter the edge: ').split())
    g[x].append(y)
    g[y].append(x)

for i in range(1, n+1):
    b[i] = int(input('Enter the value of node: '))

visited = [0] * (n+1)
parent = [0] * (n+1)
sums = [0] * (n+1)
dfsSum(1, g, visited, parent, sums, b)

for i in range(1, n+1):
    print(sums[i], end=' ')