class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid 
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1

s = Solution()
a = s.search([2, 5, 8, 12, 16, 23, 38, 56],23)
print(a)