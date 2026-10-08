class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            while stack and k >0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k>0:
            stack.pop()
            k -= 1
        
        result = ''.join(stack)
        result = result.lstrip('0') or '0'
        return result

        