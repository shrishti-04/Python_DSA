# Find the maximum summation product of two arrays

def maxSummationProduct(a, b):
    a.sort()
    b.sort()

    max_product_sum = 0
    n = len(a)

    for i in range(n):
        max_product_sum += a[i] * b[i]

    return max_product_sum

a = [1, 2, 3, 4]
b = [-1, 4, 5, 6]
print(maxSummationProduct(a, b))