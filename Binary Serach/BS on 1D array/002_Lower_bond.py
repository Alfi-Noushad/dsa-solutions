class Solution:
    def lowerBound(self, nums, x):
       low = 0
       high = len(nums)-1
       ans = 0

       while low <= high:
           mid = (low + high) //2

           if x <= nums[mid]:
               ans = mid
               high = mid -1
           else:
               low = mid+1
       return ans
    
s = Solution()
a = s.lowerBound([3,5,8,15,19],9)
print(a)
               



