# # Print the given pattern
# # 000000
# # 000000
# # 000000
# # 000000
# # 000000

n = int(input("Enter your number: "))

for i in range(5):
    for j in range(6):
        print(0, end='')
    print('')
    
# # Print the given pattern
# # 0
# # 00
# # 000
# # 0000
# # 00000

n = int(input("Enter your number: "))

for i in range(n):
    for j in range(i+1):
        print(0, end='')
    print('')

# # Print the given pattern

# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5

n = int(input("Enter your number: "))

for i in range(n):
    for j in range(i+1):
        print(i+1, end='')
    print('')

# # Print the given pattern

# # A
# # BB
# # CCC
# # DDDD
# # EEEEE
# # FFFFFF

n = int(input("Enter your number: "))

for i in range(n):
    for j in range(i+1):
        print(chr(65 + i), end='')
    print('')
    
# # Print the given pattern

# # A
# # B C
# # C D E
# # D E F G

n = int(input("Enter your number: "))

for i in range(n):
    for j in range(i+1):
        print(chr(65 + j + i), end='')
    print('')

# # Print the given pattern

# # E
# # D E
# # C D E
# # B C D E
# # A B C D E

n = int(input("Enter your number: "))

for i in range(n):
    for j in range(i+1):
        # Accordint to ASCII A = 65, so therefore E = 69
        print(chr(69 + j - i), end='')
    print('')

# # Print the given pattern

# #      1
# #     12
# #    123
# #   1234

n = int(input('Enter your number: '))

for i in range(n):
    print(' '*(n-i), end='')
    for j in range(i+1):
        print(j+1, end='')
    print('')
    
# # Print the given number

# # 55555 
# # 4444
# # 333
# # 22
# # 1

n = int(input('Enter your number: '))

for i in range(n, 0, -1):
    for j in range(i):
        print(i, end='')
    print('')

# # Print the given number:

# #   *
# #  ***
# # *****
# # *****
# #  ***
# #   *

n = int(input('Enter your number: '))

for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    for j in range(n-i-1):
        print(' ', end='')
    print('')
    
for k in range(n):
    for l in range(k):
        print(' ', end='')
    for l in range(2*n - (2*k + 1)):
        print('*', end='')
    for l in range(k):
        print(' ', end='')
    print('')

# # print a pattern like this

#     #        1
#     #       232
#     #      34543
#     #     4567654
#     #    567898765
    
n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(1, 2*i+2):
        br = (2*i+1) // 2
        if (j <= br + 1):
            print(j+i, end='')
        else:
            print((2*i+2) - (j - i), end='')
    for j in range(n-i-1):
        print(' ', end='')
    print('')

# # Print a pattern like this:

# # ****
# # *  *
# # *  *
# # ****

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        if ((i == 0) or (i == n-1) or (j == 0) or (j == n-1)):
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# # Print a pattern like this:

# # 4444444
# # 4333334
# # 4322234
# # 4321234
# # 4322234
# # 4333334
# # 4444444

n = int(input('Enter a number'))

for i in range(2*n-1):
    for j in range(2*n-1):
        
        top = i
        left = j
        right = ((2*n - 1) - 1) - j
        bottom = ((2*n - 1) - 1) - i
        
        print(n - min(min(left, right), min(top, bottom)), end = ' ' )
        
    print('')

# #  Print a pattern like this:

# # ****
# #  ****
# #   ****
# #    ****

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n+i-1):
        print(' ', end = '')
    for j in range(n):
        print('*', end = '')
    print('')
    
# # Print a pattern like this:

# # 1=1
# # 1+2=3
# # 1+2+3=6
# # 1+2+3+4=10

n = int(input('Enter a number: '))

for i in range(n):
    result = 0
    for j in range(1, i+2):
        print(j, end='')
        if (j < i+1):
            print('+', end='')
        result += j
    print('=' + str(result))

# # Print a pattern like this:

# # 1357
# # 3571
# # 5713
# # 7135

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(2*i+1, 2*n, 2):
        print(j, end='')
    a = 1
    for k in range(i):
        print(a, end='')
        a += 2
    print('')
    
# # Print a pattern like this

# # * * * * * *
# # *       *
# # *     *
# # *   *
# # * *
# # *

n = int(input('Enter a number: '))

for i in range(n, 0, -1):
    for j in range(i):
        if (i == n or j == 0 or j == i-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')

# Print a pattern like this:

#         * 
#       *   * 
#     *       * 
#   *           * 
# * * * * * * * * * 

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    for j in range(2*i+1):
        if (i == n-1 or j == 0 or j == 2*i):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')