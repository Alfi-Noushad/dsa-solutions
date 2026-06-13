class Solution:
    def pattern21(self, n):
        for i in range(1,n+1):  #row
            for j in range(1,n+1):  #column
                if i==1 or i == n or j==1 or j==n:
                    print("*",end="")
                else: 
                    print(" ",end="")
            print()
               


c = Solution()
c.pattern21(5)



"""

*****
*   *
*   *
*   *
*****

"""