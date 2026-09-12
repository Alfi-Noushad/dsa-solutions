class Solution:
    def checktype(self,n):
        mask = 1 >> 0
        if n & mask == 0:
            return True
        else:
            return False

s = Solution()
a = s.checktype(8)
print(a)
