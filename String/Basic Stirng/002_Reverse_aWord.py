class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        i = len(s)-1
        it = len(s)
        while i >= 0:
            if s[i] != " ":
                i -= 1
            else:
                result += s[i+1:it] + " "
                it = i
                i -= 1
        result += s[:it]
        return result


sol = Solution()
print(sol.reverseWords("hello world"))