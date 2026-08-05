class Solution:
    def sorts(self,stack):
        if not stack:
            return
        top = stack.pop()
        self.sorts(stack)

        self.insert(stack,top)

    def insert(self,stack,x):
        if not stack or x <= stack[-1]:
            stack.append(x)
            return

        temp = stack.pop()
        self.insert(stack,x)

        stack.append(temp)

stack = [4, 1, 3, 2]
s = Solution()
s.sorts(stack)

print(stack)