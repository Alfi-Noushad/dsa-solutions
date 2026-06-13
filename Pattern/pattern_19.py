class Solution:
    def pattern19(self, n):
        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print("*",end="")

            for j in range(2*(n-i)):
                print(" ",end="")

            for j in range(i,0,-1):
                 print("*",end="")
            print()

        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")

            for j in range(2*(n-i)):
                print(" ",end="")
            
            for j in range(i):
                print("*",end="")
            print()


c = Solution()
c.pattern19(5)


"""

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********


"""