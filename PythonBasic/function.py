# WAF to print the length of list

cities = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Pune']

def len_list(list):
    return len(list)

print(len_list(cities))

# WAF to print the elements of the lists

alpha = ['a', 'b', 'c', 'd', 'e', 'f']

def ele(list):
    i = 0
    while(i < len(list)):
        print(list[i], end=', ')
        i += 1
        
ele(alpha)
    
# Using for loop

def ele(list):
    for i in list:
        print(i, end=', ')
        
ele(alpha)

# WAF to find the factorial of n

def fact_num(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact
    
print(fact_num(5))
print(fact_num(7))

# WAF to convert the USD into INR

def converter(USD_value):
    INR_value = USD_value * 83
    print(USD_value, 'USD = ', INR_value, 'INR')
    
converter(4)

#  WAF in order to check whether given number is odd or even

def odd_even(n):
    if n % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
        
odd_even(10)