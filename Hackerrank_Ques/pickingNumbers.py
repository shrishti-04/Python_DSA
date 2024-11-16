# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

# Example
# a = [1, 1, 2, 2, 4, 4, 5, 5, 5]

# There are two subarrays meeting the criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray has 5 elements.

def pickingNumbers(a):
    a.sort()
    maxlen = 1
    
    for i in range(len(a)):
        maxi = a[i]
        mini = a[i]
        
        for j in range(i + 1, len(a)):
            maxi = max(maxi, a[j])
            mini = min(mini, a[j])
            
            if(maxi - mini <= 1):
                current_len = j-i+1
                maxlen = max(maxlen, current_len)
                
    return maxlen

result = pickingNumbers([1, 2, 2, 3, 1, 2])
print(result)