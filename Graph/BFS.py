# BFS is Breadth first search algorithm which is used to traverse the graph level by level.
# Here is the code which will traverse the graph using BFS algorithm:

from queue import Queue

n = int(input('Enter the number of nodes: '))
m = int(input('Enter the number of edges: '))

g = [[]*n for i in range(n+5)]

for i in range(m):
    x = int(input('Enter the first node: '))
    y = int(input('Enter the second node: '))
    g[x].append(y)
    g[y].append(x)

q = Queue()
q.put(1)

visited = [0]*(n+5)
visited[1] = 1
level = [0]*(n+5)
level[1] = 0

while not q.empty():
    # BFS algorithm
    x = q.get()
    print(x, level[x])

    for y in (g[x]):
        if(visited[y] == 0):
            q.put(y)
            visited[y] = 1
            level[y] = level[x] + 1

# This code will take input of graph and then traverse the graph using BFS algorithm.

# Output:

# Enter the number of nodes: 7
# Enter the number of edges: 8
# Enter the first node: 1
# Enter the second node: 2
# Enter the first node: 1
# Enter the second node: 3
# Enter the first node: 1
# Enter the second node: 4
# Enter the first node: 2
# Enter the second node: 5
# Enter the first node: 3
# Enter the second node: 5
# Enter the first node: 3
# Enter the second node: 6
# Enter the first node: 4
# Enter the second node: 6
# Enter the first node: 6
# Enter the second node: 7
# 1 0
# 2 1
# 3 1
# 4 1
# 5 2
# 6 2
# 7 3

# The graph is:

#     1
#  /  |  \
# 2   3   4
#  \ / \ /
#   5   6
#       |
#       7