# code

def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        mini = i
        for j in range(i, n):
            if(arr[j] < arr[mini]):
                mini = j
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp

    return arr

result = selectionSort([8, 4, 9, 3, 5, 1])
print(result)