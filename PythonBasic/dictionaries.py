# Store following word meanings in a python dictionaries:
# table: 'a piece of furniture', 'list of facts & figures'
# cat: 'a small animal'

# dict = {'table': ['a piece of furniture', 'list of facts & figures'],
#         'cat': 'a small animal'}

# print(dict)

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject names as key & mark as value.

marks = {}

phy = int(input('Enter your physics marks: '))
marks.update({'Physics': phy})

chem = int(input('Enter your chem marks: '))
marks.update({'Chemistry': chem})

maths = int(input('Enter your maths marks: '))
marks.update({'Maths': maths})

print(marks)