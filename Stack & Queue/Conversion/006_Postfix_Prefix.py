class Solution:
    def postfixToInfix(self,s):
        stack = []
        
        for ch in s:
            if ch.isalnum():
                stack.append(ch)
            else:
                # pop two
                operand1 = stack.pop()
                operand2 = stack.pop()
                # combine them
                # push result back
                stack.append( "("+ ch + operand2 +  operand1  +")" )

        return ''.join(stack)
s = Solution()
print(s.postfixToInfix("ABC*+"))