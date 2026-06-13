class Solution:
    arr = ["A","B","C","D","E","F"]
    def pattern16(self, n):
        for i in range(n+1):
            for j in range(i):
                print(self.arr[i-1],end="")
            print()


c = Solution()
c.pattern16(4)

"""

A
BB
CCC
DDDD

"""