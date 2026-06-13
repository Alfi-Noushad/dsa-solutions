class Solution:
    arr = ["A","B","C","D"]
    def pattern18(self, n):
        for i in range(n+1):
            for j in range(i,0,-1):
                print(self.arr[-j],end="")
            print()

c = Solution()
c.pattern18(4)

"""
D
CD
BCD
ABCD


"""