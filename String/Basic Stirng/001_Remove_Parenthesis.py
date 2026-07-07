class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ""
        counter = 0
        for i in range(len(s)):
            if s[i] == "(":
                if counter > 0:
                    a += '('
                counter += 1
            elif s[i] == ")":
                counter -= 1
                if counter > 0:
                    a += ')'
                #counter -= 1
        return a
s = Solution()
a= s.removeOuterParentheses("((()))")
print(a)