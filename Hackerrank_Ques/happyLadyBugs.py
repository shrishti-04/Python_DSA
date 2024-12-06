# Happy Ladybugs is a board game having the following properties:

# The board is represented by a string, b, of length n. The ith character of the string, b[i], denotes the ith cell of the board.
# If b[i] is an underscore (i.e., _), it means the ith cell of the board is empty.
# If b[i] is an uppercase English alphabetic letter (ascii[A-Z]), it means the ith cell contains a ladybug of color b[i].
# String b will not contain any other characters.
# A ladybug is happy only when its left or right adjacent cell (i.e., b[i +- 1]) is occupied by another ladybug having the same color.
# In a single move, you can move a ladybug from its current position to any empty cell.
# Given the values of n and b for g games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. 
# For each game, return YES if all the ladybugs can be made happy through some number of moves. Otherwise, return NO.

def happyLadyBugs(b):
    freq = 0
    for i in b:
        if(i == '_'):
            freq += 1

    for i in b:
        if(b.count(i) == 1 and i != '_'):
            return 'NO'
        
    for i in range(1, len(b)-1):
        if(b[i] != b[i-1] and b[i] != b[i+1] and freq != 0):
            return 'NO'
        
    return 'YES'

result = happyLadyBugs('RBY_YBR')
print(result)