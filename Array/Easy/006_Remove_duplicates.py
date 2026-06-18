class Solution:
    def removeDuplicates(self, arr):
        j =0
        for i in range(1,len(arr)):
            if arr[i] != arr[j]:
                 j += 1
                 arr[j] = arr[i]
                 
        print(arr[:j+1])
s = Solution()
s.removeDuplicates([-2, 2, 4, 4, 4, 4, 5, 5])

