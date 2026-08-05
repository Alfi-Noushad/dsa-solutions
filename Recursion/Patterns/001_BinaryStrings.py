class Solution:
    def binaryString(self, current, n):
        if len(current) == n:
            print(current)
            return

        self.binaryString(current + "0", n)
        self.binaryString(current + "1", n)

s = Solution()
s.binaryString("", 3)