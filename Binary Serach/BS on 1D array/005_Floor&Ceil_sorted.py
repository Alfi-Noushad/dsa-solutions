class Solution:
    def getFloorAndCeil(self, nums, x):
        low = 0
        high = len(nums) - 1
        floors = 0
        ceils = 0

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == x:
                floors = ceils = nums[mid]
                
            elif nums[mid] > x:
                ceils = nums[mid]
                high = mid - 1
            else:
                floors = nums[mid]
                low = mid + 1   
        return floors,ceils

s = Solution()
a = s.getFloorAndCeil([3, 4, 4, 7, 8, 10],5)
print(a)