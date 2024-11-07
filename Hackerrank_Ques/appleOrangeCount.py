# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
# Using the information given below, determine the number of apples and oranges that land on Sam's house.

# In the diagram below:

# The red region denotes the house, where s is the start point, and t is the endpoint. 
# The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
# When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. 
# *A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right. 

# Complete the countApplesAndOranges function in the editor below. It should print the number of apples 
# and oranges that land on Sam's house, each on a separate line.

# countApplesAndOranges has the following parameter(s):

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    
    for i in range(len(apples)):
        apples[i] += a
        if((apples[i] >= s) and (apples[i] <= t)):
            apple_count += 1
            
    for i in range(len(oranges)):
        oranges[i] += b
        if((oranges[i] >= s) and (oranges[i] <= t)):
            orange_count += 1
            
    print(apple_count)
    print(orange_count)
    
countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])

# logic: a = 4 (location of apple tree)
#        b = 12 (location of orange tree)
#        s = 7 (starting of sam's house)
#        t = 10 (end of sam's house)
#        m = 3 (no. of apples)
#        n = 3 (no. of oranges)
#        apples = [2, 3, -4] (dist from apple tree)
#        oranges = [3, -2, -4] (dist from orange tree)

#        add these distance points with the location of apple tree and orange tree
#        to get their landing point, and their landing point are:

#        apples = [2+4, 3+4, -4+4] = [6, 7, 0]
#        there is just one apple i.e. 7 which falls in sam's house, that is in between 7 and 10

#        oranges = [3+12, -2+12, -4+12] = [15, 10, 8]
#        there are two oranges i.e. 10 and 8 which falls in sam's house, that is in between 7 and 10

#        so the output will be 1 and 2
