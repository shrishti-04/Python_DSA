n = int(input('Enter the number of nodes: '))
m = int(input('Enter the number of edges: '))

g = [[]*n for i in range(n)]

for i in range(m):
    x = int(input('Enter the first node: '))
    y = int(input('Enter the second node: '))
    g[x].append(y)
    g[y].append(x)

for i in range(n):
    print(i, len(g[i]))