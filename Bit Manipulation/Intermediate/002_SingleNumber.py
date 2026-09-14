class Solution:
    def singleNumber(self, arr):
        x = 0
        for i in arr:
            x ^= i
        
        return x

s = Solution()
s.singleNumber([2,2,1])
        