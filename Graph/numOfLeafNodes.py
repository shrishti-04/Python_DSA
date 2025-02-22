# Q :-> Given a Tree of “N” nodes and N-1 edges ; rooted at node “1” ; print “N” integers ; 
# where the ith integer prints the number of children of the ith node. Once this is done ; 
# print all the leaves of the particular tree.

import queue

n = int(input('Enter the number of nodes: '))
g = [[] for _ in range(n+1)]

i = 1
while i < n:
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
    i += 1

q = queue.Queue()
q.put(1)
visited = [0]*(n+1)
visited[1] = 1

while not q.empty():
    x = q.get()
    count = 0
    for y in g[x]:
        if visited[y] == 0:
            count += 1
            visited[y] = 1
            q.put(y)

    print(x, count)
