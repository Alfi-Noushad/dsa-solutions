class Solution:
    def infixToPostfix(self, s):
        stack =[]
        output = []

        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

        for ch in s:
            if ch ==' ':
                continue
            elif ch.isalnum():
                output.append(ch)

            elif ch == '(':
                stack.append(ch)

            elif ch ==')':
                while stack[-1] != '(':
                        a = stack.pop()
                        output.append(a)

                stack.pop()
            else:
                while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[ch]:
                    a = stack.pop()
                    output.append(a)
                stack.append(ch)
        while stack:
            output.append(stack.pop())

        return ''.join(output)
s = Solution()
a = s.infixToPostfix('A+B*C-D')
print(a)