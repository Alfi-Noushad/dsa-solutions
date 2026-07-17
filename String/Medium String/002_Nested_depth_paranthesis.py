class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        maxdepth = 0

        for ch in s:
            if ch == '(':
                depth += 1
                maxdepth = max(maxdepth,depth)
            elif ch == ')':
                depth -= 1
            else:
                continue
        return maxdepth

s = Solution()
a = s.maxDepth("(1+(2*3)+((8)/4))+1")
print(a)