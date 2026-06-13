class Solution:
    arr = ["A","B","C","D","E","F"]
    def pattern14(self, n):
        for i in range(n+1):
            for j in range(i):
                print(self.arr[j],end="")

            print()



c = Solution()
c.pattern14(4)

"""

A
AB
ABC
ABCD

"""