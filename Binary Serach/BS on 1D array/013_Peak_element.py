class Solution(object):
    def findPeakElement(self, nums):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid+1
        return high
s = Solution()
a = s.findPeakElement([1,2,3,4,5,6,7,8,5,1])
print(a)
        