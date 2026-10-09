class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        left = [-1] *len(arr)
        right = [len(arr)] *len(arr)
        left_choices = right_choices = result = 0

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        

        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        for i in range(len(arr)):
            left_choices = i - left[i]
            right_choices = right[i] - i

            result += arr[i] * left_choices * right_choices
            
        return result % (10**9 + 7)

        