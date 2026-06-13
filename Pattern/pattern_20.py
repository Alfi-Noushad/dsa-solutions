class Solution:
    def pattern20(self, n):
        for i in range(n):
            for j in range(i):
                print("*",end="")

            for j in range(2*(n-i)):
                print(" ",end="")

            for j in range(i):
                print("*",end="")
            print()
        
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end="")

            for j in range(2*(n-i)):
                 print(" ",end="")

            for j in range(i):
                print("*",end="")
            print()


c = Solution()
c.pattern20(5)


"""

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *


"""