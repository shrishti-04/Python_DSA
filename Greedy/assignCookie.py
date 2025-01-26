# Assign cookie to children with greedily to maximize the number of content children

def findContentChildren(greed, cookieSize):
    n = len(greed)
    m = len(cookieSize)

    greed.sort()
    cookieSize.sort()

    i = 0
    j = 0

    while (i < n and j < m):
        if(greed[i] <= cookieSize[j]):
            i += 1
        j += 1

    return i

greed = [1, 2, 6, 3]
cookieSize = [1, 3, 1]
print(findContentChildren(greed, cookieSize))