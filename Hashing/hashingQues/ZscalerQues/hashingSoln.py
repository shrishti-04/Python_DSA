# You are given an array “A”; in one step select largest element of array and convert it to second largest element of the array 
# Tell the minimum number of steps such that all elements become equal

# The above code is the solution to the Zscaler Interview Question just in Hashing method.

from collections import defaultdict
def main():
    n = int(input('Enter the length of the array: '))
    a = [0] * (n+1)

    for i in range(n+1):
        a[i] = int(input('Enter the element: '))

    k = defaultdict(int)

    for i in range(1, n+1):
        k[a[i]] += 1

    g = sorted(k.items(), key = lambda x: x[0], reverse = True)

    size = len(g)
    steps = 0

    for i in range(size-1):

        new_a = []
        for x in a:
            if(x == g[i][0]):
                new_a.append(g[i+1][0])
            else:
                new_a.append(x)
        a = new_a

        g[i+1] = (g[i+1][0], g[i+1][1] + g[i][1])
        steps += g[i][1]

        g[i] = (g[i][0], 0)

    

    print('new array:', new_a)
    print('Steps required:', steps)

main()

