class Solution(object):
    MOD = 10**9 + 7

    def power(self, x, n):
        if n == 0:
            return 1

        half = self.power(x, n // 2)

        if n % 2 == 0:
            return (half * half) % self.MOD
        else:
            return (half * half * x) % self.MOD

    def countGoodNumbers(self, n):
        """ 
        :type n: int
        :rtype: int 
        """
        even = (n + 1) // 2
        odd = n // 2

        ans = (self.power(5, even) * self.power(4, odd)) % self.MOD
        return ans