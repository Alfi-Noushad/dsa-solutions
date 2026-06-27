def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid + 1

    count = 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            count += (mid - left + 1)
            right+=1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        for i in range(low,high+1):
            arr[i] = temp[i-low]
        
        return count
def mergeSort(arr,low,high):
    count = 0

    if low >= high:
        return count
    
    mid = (low+high)//2

    count += mergeSort(arr, low, mid)
    # Count inversions in right half
    count += mergeSort(arr, mid + 1, high)
    # Count inversions during merge
    count += merge(arr, low, mid, high)

    return count


def numberOfInversions(arr):
    return mergeSort(arr, 0, len(arr) - 1)


a = [5, 4, 3, 2, 1]

count = numberOfInversions(a)
print(count)