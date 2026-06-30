class Solution:
    def upperBound(self, nums, x):
       low = 0
       high = len(nums)-1
       ans = 0

       while low <= high:
           mid = (low + high) //2

           if x < nums[mid]:
               ans = mid
               high = mid -1
           else:
               low = mid+1
       return ans
    
s = Solution()
a = s.upperBound([1,2,2,3],2)
print(a)
               



