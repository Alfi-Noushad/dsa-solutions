class Solution:
    def singleNumber(self, arr):
        x = 0
        for i in arr:
            x ^= i
        
        print(x)

s = Solution()
s.singleNumber([1, 2, 2, 4, 3, 1, 4])
        