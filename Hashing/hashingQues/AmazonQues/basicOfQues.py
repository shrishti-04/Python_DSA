# First we will do Basic Question using hashing method

# def maxSubarraySum(b):
#     n = len(b) - 1
#     if(n == 0):
#         return 0
    
#     P1 = [0] * (n + 1)

#     for i in range(1, n+1):
#         P1[i] = max(P1[i-1] + b[i], b[i], 0)
#         print(P1[i])

#     maxSum = P1[1]
#     for i in range(2, n+1):
#         if(P1[i] > maxSum):
#             maxSum = P1[i]

#     return maxSum

# b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('Maximum Subarray is:', maxSubarraySum(b))

# Now we will implement the same using kadane's algorithm

# def maxSubarraySumKadane(b):
#     n = len(b) - 1
#     if(n == 0):
#         return 0
    
#     T = 0
#     current = 0

#     for i in range(1, n+1):
#         current = max(current + b[i], b[i], 0)
#         T = max(T, current)

#     return T

# b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('Maximum Subarray is:', maxSubarraySumKadane(b))