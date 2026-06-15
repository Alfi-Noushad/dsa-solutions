class Solution:
    def GCD(self, n1, n2):
        gcd = min(n1,n2)
        for i in range(1,gcd+1):
            if n1%i == 0 and n2%i == 0:
                gcd = i

        print(gcd)

s = Solution()
s.GCD(20,15)
       

#TC: O(min(n1, n2))
#SP: O(1)        