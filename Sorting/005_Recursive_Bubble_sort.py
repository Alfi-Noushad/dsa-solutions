def bubbleSort(arr,n):
    if n == 1:
        return
    
    for j in range(n-1):
        if arr[j] >= arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

    bubbleSort(arr,n-1)

arr = [64,25,12,22,11]
bubbleSort(arr,len(arr))
print(arr)