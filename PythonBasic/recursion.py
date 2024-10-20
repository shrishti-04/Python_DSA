# WAF to find the factorial of n

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n-1) * n
    
print(fact(5))

# Write a recursive function to calculate the sum of first n natural numbers

def total(n):
    if(n == 0):
        return 0
    return total(n-1) + n

print(total(5))

# Write a recursive function to print all elements in a list

def ele(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    ele(list, idx+1)
    
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print(ele(fruits))