class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for current in asteroids:
            alive =True
            while stack and stack[-1] > 0 and current < 0:
                if stack[-1] < -current:
                    stack.pop()
                    continue

                elif stack[-1] == -current:
                    stack.pop()
                    alive = False
                    break
                else:
                    alive =False
                    break
            if alive:
                stack.append(current)
        return stack
