class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        left = [-1]*len(nums)
        right = [len(nums)]*len(nums)
        result = 0
        maximum = 0
        minimum = 0

        #right
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1]

            stack.append(i)
        
        stack = []

        #left boundary
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1]

            stack.append(i)
        for i in range(len(nums)):
            left_choices = i - left[i]
            right_choices = right[i] - i
            maximum += nums[i] * left_choices * right_choices

        # minimum
        stack = []
        left = [-1] * len(nums)
        right = [len(nums)] * len(nums)


        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)
        
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        for i in range(len(nums)):
            left_choices = i - left[i]
            right_choices = right[i] - i
            minimum += nums[i] * left_choices * right_choices

        return maximum - minimum



        