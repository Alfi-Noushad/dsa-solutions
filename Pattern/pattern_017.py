class Solution:
    arr = ["A","B","C","D","E","F"]
    def pattern17(self, n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ",end="")
            
            for j in range(i):
                print(self.arr[j],end="")
            for j in range(i-1,0,-1):
                print(self.arr[j-1],end="")

            print()


c = Solution()
c.pattern17(4)


"""

   A
  ABA
 ABCBA
ABCDCBA

"""