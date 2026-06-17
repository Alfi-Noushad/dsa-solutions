def Quicksort(arr, low, high):
    if low >= high:
         return

   
    pivot = arr[low]
    i = low
    j = high
    while i < j:

        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i < j:
                arr[i],arr[j] = arr[j],arr[i]
        p = j
    arr[low], arr[j] = arr[j], arr[low]
    
    Quicksort(arr,low,p-1)
    Quicksort(arr,p+1,high)

arr = [4,6,2,5,7,9,1,3]
Quicksort(arr,0,len(arr)-1)
print(arr)

