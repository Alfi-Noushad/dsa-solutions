class Solution:
    def countOcu(self, nums, target):
        low = 0
        high = len(nums)-1
        resultL = -1
        resultF = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                resultL = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                resultF = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return resultL-resultF+1

s = Solution()
a = s.countOcu([3, 4, 13, 13, 13, 20, 40],13)
print(a)