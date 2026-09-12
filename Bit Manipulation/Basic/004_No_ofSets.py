class Solution:
    def sets(self,n):
        count =0
        while n != 0:
            count += 1
            n = n & (n-1)

        return count
s = Solution()
a = s.sets(13)
print(a)
