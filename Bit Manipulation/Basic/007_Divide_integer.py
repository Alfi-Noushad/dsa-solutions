class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n = divisor
        quo =0
        while dividend >= divisor:
            i = 0
            while divisor << (i + 1) <= dividend:
                i += 1
            
            dividend -= divisor << i

            quo += 1 << i

        return quo

s = Solution()
a = s.divide(25,4)
print(a)


                
        