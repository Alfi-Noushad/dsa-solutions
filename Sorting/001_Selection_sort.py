class Solution:
    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n):
            min_i = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_i]:
                    min_i = j
            
            temp = arr[i]
            arr[i] = arr[min_i]        #arr[i], arr[min_i] = arr[min_i], arr[i]
            arr[min_i] = temp
        

        print(arr)

s = Solution()
s.selectionSort(arr=[64,25,12,22,11])

#Time Complexity: O(n²)
#Space Complexity: O(1)