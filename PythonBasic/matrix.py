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

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = len(arr)
col = len(arr[0])

for i in range(row):
    for j in range(col):
        if(i == 0 or i == row-1 or j == 0 or j == col-1):
            print(arr[i][j], end=' ')
            
print('')