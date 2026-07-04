class Solution:
    def findPages(self, nums, m):
       low = max(nums)
       high = sum(nums)

       while low<=high:
           mid = (low+high) // 2
           pages = 0
           student = 1
           for books in nums:
               if pages+books <= mid:
                   pages += books
               else:
                  student += 1  
                  pages = books
           if student <= m:
               high = mid - 1
           else:
               low = mid + 1
       return low

s = Solution()
a = s.findPages([12, 34, 67, 90],2)
print(a)
               

            