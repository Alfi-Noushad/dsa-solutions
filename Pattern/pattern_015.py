class Solution:
    arr = ["A","B","C","D","E","F"]
    def pattern15(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print(self.arr[j],end="")
            print()


c = Solution()
c.pattern15(4)

"""
ABCD
ABC
AB
A

"""
