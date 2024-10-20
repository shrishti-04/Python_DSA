# WAP to check if a number entered by the user is odd or even.
# Solution:

num = int(input('Enter a number: '))

if(num % 2 == 0):
    print('Entered number is Even')
else:
    print('Entered number is Odd')

# WAP to find the greatest of 3 numbers entered by the user
# Solution:

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
num3 = int(input('Enter your third number: '))

if(num1 >= num2 and num1 >= num3):
    print('num1 is the greatest of 3 numbers entered by the user', num1)
elif(num2 >= num3):
    print('num2 is the greatest of 3 numbers entered by the user', num2)
else:
    print('num3 is the greatest of 3 numbers entered by the user', num3)
    
# WAP to find the greatest of 4 numbers entered by the user
# Solution:

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))
d = int(input('Enter your forth number: '))

if(a >= b and a >= c and a >= d):
    print('a is the greatest of 4 numbers entered by the user', a)
elif(b >= c and b >= d):
    print('b is the greatest of 4 numbers entered by the user', b)
elif(c >= d):
    print('c is the greatest of 4 numbers entered by the user', c)
else:
    print('d is the greatest of 4 numbers entered by the user', d)

# WAP to check if a number is a multiple of 7

num = int(input('Enter a number:'))

if(num % 7 == 0):
    print('num is a multiple of 7')
else:
    print('num is not a multiple of 7')