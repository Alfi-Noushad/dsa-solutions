class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
             mid = (low + high) // 2

             if nums[mid] == target:
                 return mid
             #checks the left half is sorted first
             if nums[low] <= nums[mid]:
                 if nums[low] <= target < nums[mid]:
                     high = mid - 1
                 else:
                     low = mid + 1
             else:
                  if nums[mid] < target <= nums[high]:
                      low = mid + 1
                  else:
                      high = mid - 1
        return -1

s = Solution()
a = s.search([4,5,6,7,0,1,2],0)
print(a)
