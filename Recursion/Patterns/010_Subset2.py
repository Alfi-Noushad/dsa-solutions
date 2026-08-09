class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def solve(index,current_list):
            ans.append(current_list[:])
            
            nums.sort()
            for i in range(index,len(nums)):
                if i>index and nums[i] == nums[i-1]:
                    continue
                current_list.append(nums[i])

                solve(i + 1, current_list)

                current_list.pop()
        solve(0,[])
        return ans

        