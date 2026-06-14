class Solution:
    def countDigit(self, n):
        counts = 0
        while n > 0:
            r = n%10
            counts += 1
            n = n//10
        
        print(counts)

s = Solution()
s.countDigit(120)

#TC: O(log n)
#SP: O(1)