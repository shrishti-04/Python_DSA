# Given a tree of N nodes and N-q edges; rooted at node 1, 
# print N integers where ith integer represents the number of children of ith node. 
# Print all the leaves of particular tree.

import queue

n = int(input('enter the number of nodes: '))
g = [[] for i in range(n+1)]

for i in range(n-1):
    x, y = map(int, input('enter the edge: ').split())
    g[x].append(y)
    g[y].append(x)

q = queue.Queue()
q.put(1)

visited = [0] * (n+1)
visited[1] = 1

while(not q.empty()):
    x = q.get()
    count = 0
    for y in g[x]:
        if(visited[y] == 0):
            visited[y] = 1
            count += 1
            q.put(y)
    print(count, end=' ')
print()