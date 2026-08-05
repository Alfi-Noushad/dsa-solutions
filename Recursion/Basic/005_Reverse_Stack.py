class Solution:
    def reverse(self,stack):
        if not stack:
            return
        top = stack.pop()
        self.reverse(stack)

        self.insert_bottom(stack,top)

    def insert_bottom(self,stack,x):
        if not stack:
            stack.append(x)
            return

        temp = stack.pop()
        self.insert_bottom(stack,x)

        stack.append(temp)

stack = [4, 1, 3, 2]
s = Solution()
s.reverse(stack)

print(stack)