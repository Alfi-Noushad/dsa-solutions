class Solution:
    def sortColors(self, arr):
       low = 0
       mid = 0
       right = len(arr)-1

       while mid <= right:
           if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                mid += 1
                low += 1
           elif arr[mid] == 1:
               mid += 1
            
           else:
               arr[mid],arr[right] = arr[right],arr[mid]
               right -= 1

       print(arr)
               

s = Solution()
s.sortColors([1, 0, 2, 1, 0])




"""
class Solution:
    def sortZeroOneTwo(self, arr):
        for i in range(len(arr)):
            r = i+1
            while r < len(arr):
                if arr[i] > arr[r]:
                    arr[i],arr[r] = arr[r],arr[i]
                    r += 1
                else: 
                    r += 1
        print(arr)

s = Solution()
s.sortZeroOneTwo([1, 0, 2, 1, 0])
"""
