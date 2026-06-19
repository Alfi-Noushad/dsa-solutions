class Solution:
    def findMaxConsecutiveOnes(self, arr):
        count = 0
        maxcount = 0
        for i in arr:
            if i == 1:
                count += 1
                if maxcount < count:
                    maxcount = count
            else:
                count = 0

        print(maxcount)

s = Solution()
s.findMaxConsecutiveOnes([1, 1, 1, 1, 0, 0, 1, 1, 1, 0])
        