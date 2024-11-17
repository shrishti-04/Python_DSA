# Given a sequence of n integers, p(1), p(2),...,p(n) where each element is distinct and satisfies 1 <= p(x) <= n. 
# For each x where 1 <= x <= n, that is x increments from 1 to n, 
# find any integer y such that p(p(y)) = x and keep a history of the values of y in a return array.

# Example
# p = [5, 2, 1, 3, 4]

# Each value of x between 1 and 5, the length of the sequence, is analyzed as follows:

# x = 1 = p[3], p[4] = 3, so p[p[4]] = 1
# x = 2 = p[2], p[2] = 2, so p[p[2]] = 2
# x = 3 = p[4], p[5] = 4, so p[p[5]] = 3 
# x = 4 = p[5], p[1] = 5, so p[p[1]] = 4 
# x = 5 = p[1], p[3] = 1, so p[p[3]] = 5 
# The values for y are [4, 2, 5, 1, 3]

def sequenceEquation(p):
    result = []
    for x in range(1, len(p)+1):
        pos1 = p.index(x)+1
        pos2 = p.index(pos1)+1
        result.append(pos2)
        
    return result

permutation = sequenceEquation([5, 4, 1, 3, 6, 2])
print(permutation)