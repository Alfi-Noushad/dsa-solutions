class Solution:
    def smallestElement(self, arr):
        temp = arr[0]
        for i in range(len(arr)):
            if arr[i] < temp:
                temp = arr[i]
        
        print(temp)

s = Solution()
s.smallestElement([3, 3, 6, 1])

#tc O(n)
#sp O(1)
