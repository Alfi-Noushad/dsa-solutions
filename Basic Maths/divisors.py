class Solution:
    def divisors(self, n):
        l = []
        for i in range(1,n+1):
            if n%i == 0:
                l.append(i)

        print(l)

s = Solution()
s.divisors(6)

#TC: O(n)
#SP: O(log n)