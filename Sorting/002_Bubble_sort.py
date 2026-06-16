class Solution:
    def bubbleSort(self,arr):
        n = len(arr)

        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        
        print(arr)

s =  Solution()
s.bubbleSort(arr=[64,25,12,22,11])