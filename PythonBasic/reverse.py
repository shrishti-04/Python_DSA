# Reverse number
n = int(input('Enter a number'))

rev_num = 0
while(n > 0):
    last_digit = n % 10
    rev_num = (rev_num * 10) + last_digit
    n = n // 10
    
print(rev_num)
    
# Reverse number summation between range

s = int(input('Enter your first number: '))
e = int(input('Enter your second number: '))

rev_sum = 0

for i in range(s, e+1):
    rev = 0
    num = i
    while (num > 0):
        last_digit = num % 10
        rev = (rev * 10) + last_digit
        num = num // 10
    rev_sum += rev
        
print(rev_sum)    