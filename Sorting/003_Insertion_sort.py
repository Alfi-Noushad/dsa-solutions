class Solution:
    def insertionSort(self,arr):
        n = len(arr)

        for i in range(1,n):
            #asume first element key(sorted list)
            key = arr[i]
            j = i-1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        print(arr)
s = Solution()
s.insertionSort(arr=[64,25,12,22,11])
