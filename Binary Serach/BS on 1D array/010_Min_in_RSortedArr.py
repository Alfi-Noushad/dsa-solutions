class Solution:
    def search(self, nums):
        low = 0
        high = len(nums)-1

        while low < high:
             mid = (low + high) // 2

             if nums[mid] > nums[high]:
                 low = mid + 1
             else:
                 high = mid
             
        return nums[low]

s = Solution()
a = s.search([4,5,6,7,0,1,2,3])
print(a)
