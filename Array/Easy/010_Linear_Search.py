class Solution:
    def linearSearch(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                val = i
                break
        print(val)

s = Solution()
s.linearSearch([2, 3, 4, 5, 3],3)
