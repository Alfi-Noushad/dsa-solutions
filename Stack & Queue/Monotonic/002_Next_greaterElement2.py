class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [-1] * len(nums)
        stack = []

        for i in range(2* len(nums)):
            num = nums[i % len(nums)]

            while stack and num > nums[stack[-1]]:
                output[stack.pop()] = num
            if i<len(nums):
                stack.append(i)
        return output

        