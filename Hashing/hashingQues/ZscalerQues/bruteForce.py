# You are given an array “A”; in one step select largest element of array and convert it to second largest element of the array 
# Tell the minimum number of steps such that all elements become equal

# The above code is the solution to the Zscaler Interview Question.

def minStepstoMakeArrayEqual(a):
    n = len(a)
    if(n <= 1):
        return 0
    
    steps = 0

    while(len(set(a)) > 1):
        largest = max(a)

        secondLargest = float('-inf')
        for x in a:
            if(x != largest):
                secondLargest = max(secondLargest, x)

        for i in range(n):
            if(a[i] == largest):
                a[i] = secondLargest

        steps += 1

    return steps, a

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
steps, a = minStepstoMakeArrayEqual(a)
print('Steps required:', steps)
print('Final Array:', a)