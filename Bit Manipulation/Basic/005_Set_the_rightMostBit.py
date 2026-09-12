class Solution:
    def rightMostBit(self,n):
        mask = 1
        a = n | mask
        return n | mask

s = Solution()
a = s.rightMostBit(10)
print(a)