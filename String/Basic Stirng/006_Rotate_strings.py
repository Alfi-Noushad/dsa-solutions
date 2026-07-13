class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False 
        else:
            if goal in (s+s):
                return True
            
s = Solution()
a = s.rotateString("rotation","tionrota")
print(a)