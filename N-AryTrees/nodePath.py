# Given a tree with n nodes, rooted at node 0 (nodes are numbered from 0 to n-1), 
# with values assigned to nodes such that the values [i] denotes the value of node i,
# find the maximal sum of the values along any path starting at node u & going only downwards in the tree.

def dfsSumMax(node, g, visited, parent, sums):

    visited[node] = 1

    s = 0
    for x in g[node]:
        if(visited[x] == 0):
            parent[x] = node
            dfsSumMax(x, g, visited, parent, sums)
            s = max(s, sums[x])

    sums[node] = b[node] + s

n = int(input('enter the number of nodes: '))
g = [[] for _ in range(n)]
b = [0] * (n)

for i in range(n-1):
    x, y = map(int, input('Enter the edge:').split())
    g[x].append(y)
    g[y].append(x)

for i in range(n):
    b[i] = int(input('Enter the value of node: '))

visited = [0] * (n)
parent = [0] * (n)
sums = [0] * (n)
dfsSumMax(1, g, visited, parent, sums)

answer = 0
for i in range(1, n):
    answer = max(answer, sums[i])

print(sums)
print(answer)