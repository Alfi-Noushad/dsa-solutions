class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        count = 0
        n =  start ^ goal
        while n!=0:
            n = n & (n-1)
            count += 1
        return count


        