# Find Sum of all the Numbers from 0 till N.

def sum_num_recursive(n):
    if(n == 0):
        return 0
    else:
        return n + sum_num_recursive(n-1)
    
n = 10
result = sum_num_recursive(n)
print(result)