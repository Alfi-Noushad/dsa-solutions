class Solution(object):
    def fourSum(self, nums,target):
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i]+ nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i],nums[j],nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result


s = Solution()
print(s.fourSum([-1,0,1,2,-1,-4],3))