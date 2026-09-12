class Solution:
    def swap(self,a,b):
        a = a^b
        b = a^b
        a = a^b
        return a,b
s = Solution()
a = s.swap(2,3)
print(a)