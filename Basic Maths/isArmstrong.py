class Solution:
    def isArmstrong(self, n):
        sums = 0
        org = n
        counts = 0

        while n > 0:            #counts = len(str(n))
            r = n%10
            counts += 1
            n = n//10
        n = org
        while n > 0:
            r = n%10
            sums += r**counts
            n = n//10
        if (org == sum):
            print("is amstrong")

s = Solution()
s.isArmstrong(153)


#TC: O(log n)
#SP: O(1)        