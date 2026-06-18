class Solution:
    def largestElement(self, arr):
        temp = arr[0]
        for i in range(len(arr)):
            if arr[i] >= temp:
                temp = arr[i]
        
        print(temp)

s = Solution()
s.largestElement([3, 3, 6, 1])

#tc O(n)
#sp O(1)
