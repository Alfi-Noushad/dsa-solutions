def insertionSort(arr,n):
    if n <= 0:
        return
    
    j = n -1
    insertionSort(arr,n-1)
    while j > 0 and arr[j-1] > arr[j]:
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j -= 1

    

arr = [64,25,12,22,11]
insertionSort(arr,len(arr))
print(arr)