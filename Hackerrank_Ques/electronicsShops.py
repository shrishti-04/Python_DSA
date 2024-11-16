# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. 
# Given price lists for keyboards and USB drives and a budget, find the cost to buy them. 
# If it is not possible to buy both items, return -1.

# Example
# b = 60
# keyboards = [40, 50, 60]
# drives = [5, 8, 12]

# The person can buy a 40 keyboard + 12 USB drive = 52, or a 50 keyboard + 8 USB drive = 58. 
# Choose the latter as the more expensive option and return 58.

def getMoneySpent(keyboard, drive, budget):
    lis = []
    
    for i in keyboard:
        for j in drive:
            if(i+j <= budget):
                lis.append(i+j)
                
    if(len(lis) == 0):
        return -1
    return max(lis)
    
result1 = getMoneySpent([40, 50, 60], [5, 8, 12], 60)
result2 = getMoneySpent([10, 15, 8], [2, 4, 7], 5)

print(result1)
print(result2)