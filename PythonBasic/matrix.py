# Print the array in the form of 2d matrix

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# row = len(arr)
# col = len(arr[0])

# for i in range(row):
#     for j in range(col):
#         print(arr[i][j], end=' ')
#     print('')

# Print the left and right diagonal

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# row = len(arr)
# col = len(arr[0])

# for i in range(row):
#     for j in range(col):
#         if(i == j):
#             print(arr[i][j], end=' ')
            
# print('')
    
# for i in range(row):
#     for j in range(col):
#         if((i+j) == (row-1) and i != j):
#             print(arr[i][j], end=' ')

# Print the boundary elements

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# row = len(arr)
# col = len(arr[0])

# for i in range(row):
#     for j in range(col):
#         if(i == 0 or i == row-1 or j == 0 or j == col-1):
#             print(arr[i][j], end=' ')
            
# print('')

# Print the matrix in Z form

# arr = [[1,2,3], [4,5,6], [7,8,9]]
# row = len(arr)
# col = len(arr[0])

# for i in range(col):
#     print(arr[0][i], end=' ')
    
# i = 1
# j = col-2

# while(i < row and j >= 0):
#     print(arr[i][j], end=' ')
    
#     i+=1
#     j-=1
    
# for i in range(1, row):
#     print(arr[row-1][i], end=' ')

# Print the transpose of the matrix

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rows = len(arr)
# cols = len(arr[0])

# for i in range(rows):
#     for j in range(cols):
#         arr[i][j] = arr[j][i]
        
# for i in range(rows):
#     for j in range(cols):
#         print(arr[i][j], end=' ')
#     print('')

# Print the matrix in snake format

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(arr)
cols = len(arr[0])

for i in range(rows):
    if(i % 2 == 0):
        for j in range(cols):
            print(arr[i][j], end=' ')
    else:
        for j in range(cols-1, -1, -1):
            print(arr[i][j], end=' ')
    print('')