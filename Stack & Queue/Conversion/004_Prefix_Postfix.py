class Solution:
    def prefixToPostfix(self,s):
        stack = []

        for ch in reversed(s):
            if ch.isalnum():
                stack.append(ch)
            else:
                # pop two
                operand1 = stack.pop()
                operand2 = stack.pop()
                # combine them
                # push result back
                stack.append(  operand1 + operand2 + ch  )

        return ''.join(stack)
s = Solution()
print(s.prefixToPostfix("+A*BC"))