# Take input of graph; then tell for each node “i” how many nodes are directly connected to it.

n, m = map(int, input().split())
b = [[0]*10000 for i in range(10000)]

for i in range(1, m+1):
    x, y = map(int, input().split())
    b[x][y] = 1
    b[y][x] = 1
    
for i in range(n):
    count = 0
    for j in range(n):
        if(b[i][j] == 1):
            count += 1

    print(count)

