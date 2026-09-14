class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(2**len(nums)):
            add = []
            mask = i
            for j in range(len(nums)): 
                if mask & (1 << j):
                    add.append(nums[j])
            result.append(add)
        return result
        
        