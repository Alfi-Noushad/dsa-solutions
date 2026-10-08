class Solution(object):
    def smallElement(self, num):
        """
        :type num: str
        :rtype: str
        """
        stack = []
        result = [-1] * len(num)

        for i in range(len(num)-1,-1,-1):
            while stack and stack[-1] >= num[i]:
                stack.pop()
            

            if stack:
                result[i] = stack[-1]

            stack.append(num[i])

        return result



s = Solution()
print(s.smallElement([4, 8, 5, 2, 25]))

        