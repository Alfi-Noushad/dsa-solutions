class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            if ch in ")]}":
                if not stack or stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False
        