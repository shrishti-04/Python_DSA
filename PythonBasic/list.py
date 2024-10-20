# WAP to ask the user to enter name of their 3 favourite movies & store them in the list
# Solution:

movies = []
a = input('Enter your first movie: ')
b = input('Enter your second movie: ')
c = input('Enter your third movie: ')

movies.append(a)
movies.append(b)
movies.append(c)

print('My favourite movies are: ', movies)

# WAP to check if a list contains a palindrome of elements
# Solution:

pal = []

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))

pal.append(a)
pal.append(b)
pal.append(c)

if(pal == pal[::-1]):
    print('The specified number is palindrome')
else:
    print('The specified number is not palindrome')

# another method:

list1 = [1, 2, 2, 1]

copy_1 = list1.copy()
copy_1.reverse()

if(copy_1 == list1):
    print('Palindrome')
else:
    print('NOT Palindrome')