# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
# Example

# arr = [1, 1, 0, -1, -1]

# There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. Results are printed as:

# 0.400000
# 0.400000
# 0.200000

arr = [-4, 3, -9, 0, 4, 1]

n = len(arr)
pos = 0
neg = 0
zeroes = 0

for i in range(n):
    if(arr[i] == 0):
        zeroes += 1
    elif(arr[i] < 0):
        neg += 1
    else:
        pos += 1
        
pos = round(pos/n, 6)
neg = round(neg/n, 6)
zeroes = round(zeroes/n, 6)

print(pos)
print(neg)
print(zeroes)