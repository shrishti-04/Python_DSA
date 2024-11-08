# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

# Example
# x1 = 2
# v1 = 1
# x2 = 1
# v2 = 2

# After one jump, they are both at x=3, (x1+v1=2+1, x2+v2=1+2), so the answer is YES.

# Complete the function kangaroo in the editor below.

# kangaroo has the following parameter(s):

# int x1, int v1: starting position and jump distance for kangaroo 1
# int x2, int v2: starting position and jump distance for kangaroo 2
# Returns

# string: either YES or NO

def kangaroo(x1, v1, x2, v2):
    
    if(v1 <= v2):
        return 'NO'
    
    x = x2 - x1
    v = v1 - v2
    if(x%v == 0):
        return 'YES'
    else:
        return 'NO'
    

# LOGIC:
# we know that the formula for velocity is distance/time
# v = d/t, since v=3 in one jump step
# therefore, v = 3/1
# each jump step takes one sec, like 1 second = 1 jump, so we can do changes in velocity formula i.e.
# v = dist/jump, therefore, dist = v*jump
# to get the position we need to add all the positions with the distance in number line i.e.
# position of Kangaroo 1, pos1 = x1 + d, pos1 = x1 + v1*j
# position of Kangaroo 2, pos2 = x2 + d, pos2 = x2 + v2*j
# on equating both the equations, x1 + v1*j = x2 + v2*j
# x2 - x1 = j(v1-v2)
# j = (x2 - x1)/(v1-v2), This is the formula for jump, where jump can be 0, 1, 2
# if the remainder is 0, then yes, both the kangaroos met at one point, but if not 0 then kangaroos are at different positions.