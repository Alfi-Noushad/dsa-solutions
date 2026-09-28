class Solution:
    def infixToPrefix(self,s):
        #reverse
        s = s[::-1]

        result = []
        stack = []
        output = []

        precedence = {
                    '+': 1,
                    '-': 1,
                    '*': 2,
                    '/': 2,
                    '^': 3
                }

        #swap
        for ch in s:
            if ch == '(':
                result.append(')')
            elif ch == ')':
                result.append('(')
            else:
                result.append(ch)

        for ch in result:
            if ch == ' ':
                continue
            elif ch.isalnum():
                output.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack[-1] != '(':
                    output.append(stack.pop())

                stack.pop()
            else:
                while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[ch]:
                    output.append(stack.pop())
                stack.append(ch)
        while stack:
            output.append(stack.pop())

        #reverse 
        output = output[::-1]
        return ' '.join(output)
s = Solution()
a = s.infixToPrefix('( A + B ) * C')
print(a)