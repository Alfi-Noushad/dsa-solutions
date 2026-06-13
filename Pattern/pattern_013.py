class Solution:
    def pattern13(self, n):
        num = 1
        for i in range(n+1):
            for j in range(i):
                print(f" {num}",end="")
                num += 1
            print()
            


c = Solution()
c.pattern13(4)




"""
 1
 2 3
 4 5 6
 7 8 9 10

"""