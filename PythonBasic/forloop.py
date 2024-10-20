# Print the sum of odd and even numbers

# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# eve = 0
# odd = 0

# for i in range(len(lis)):
#     if lis[i] % 2 == 0:
#         eve += lis[i]
#     else:
#         odd += lis[i]
        
# print(odd, eve)

# Sum of pairs using single arrays

# arr=[1,2,3,4,5,6]

# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         sum = arr[i] + arr[j]
#         print(sum, end=' ')
        
# Sum of pairs using two arrays

# arr1=[1,2,3,4]
# arr2=[5,6,7,8]

# n = len(arr1)
# m = len(arr2)

# for i in range(n):
#     for j in range(m):
#         s = arr1[i] + arr2[j]
#         print(s, end=' ')

# Maximum from two arrays

# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]

# n = len(arr1)
# m = len(arr2)
# mx = 0

# for i in range(n):
#     for j in range(m):
#         s = arr1[i] + arr2[j]
#         mx = max(mx,s)
        
# print(s)

# Triplet sum

# arr = [2,3,4,5,6]
# n = len(arr)

# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             s = arr[i] + arr[j] + arr[k]
#             print(s, end=' ')

# Prime numbers in range

# s = 0
# k = 10
# prime_count = 0

# for i in range(s, k+1):
#     count = 0
#     for j in range(1, i+1):
#         if(i % j == 0):
#             count += 1
        
#     if (count == 2):
#         prime_count += 1
            
# print(prime_count)

# First and last index of a target element

arr = [1, 2, 3, 4, 5, 5, 6]
target = 5
n = len(arr)

first_idx = -1
last_idx = -1

for i in range(0, n):
    if (arr[i] == target):
        first_idx = i
        break
    
for i in range(n-1, -1, -1):
    if (arr[i] == target):
        last_idx = i
        break
    
print(first_idx, last_idx)