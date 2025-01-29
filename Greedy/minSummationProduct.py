# Find out the minimum summation product of two arrays

def minSummationProduct(a, b):
    a.sort()
    b.sort(reverse=True)
    
    min_product_sum = 0
    n = len(a)
    
    for i in range(n):
        min_product_sum += a[i] * b[i]

    return min_product_sum

a = [1, 2, 3, 4]
b = [-1, 4, 5, 6]
print(minSummationProduct(a, b))