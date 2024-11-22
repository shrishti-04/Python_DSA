# You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth.
# We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. 
# Two cells are adjacent if they have a common side, or edge.

# Find all the cavities on the map and replace their depths with the uppercase character X.

# Example
# grid = ['989', '191', '111']

# The grid is rearranged for clarity:

# 989
# 191
# 111
# Return:

# 989
# 1X1
# 111
# The center cell was deeper than those on its edges: [8,1,1,1]. 
# The deep cells in the top two corners do not share an edge with the center cell, and none of the border cells is eligible.

def cavityMap(grid):
    n = len(grid)
    grid = [list(row)   for row in grid]
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            
            cell = grid[i][j]
            top = grid[i-1][j]
            bottom = grid[i+1][j]
            left = grid[i][j-1]
            right = grid[i][j+1]
            
            if(cell > top and cell > bottom and cell > left and cell > right):
                grid[i][j] = 'X'
                
    return [''.join(row)    for row in grid]

cavity = cavityMap(['989', '191', '111'])
print(cavity)