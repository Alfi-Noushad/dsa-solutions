class Solution:
    def maxProduct(self, nums):
       prefix = 1
       suffix = 1
       ans = float('-inf')

       for i in range(len(nums)):
           
           if prefix == 0:
                prefix = 1

           if suffix == 0:
                suffix = 1

           prefix *= nums[i]
           suffix *= nums[len(nums)-1-i]

           ans = max(ans,prefix,suffix)
       return ans

s = Solution()
a = s.maxProduct([2, 3, 4])
print(a)









'''
class Solution:
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = ans = nums[0]
        for i in range(1,len(nums)):
            #base condition
            if nums[i]<0:
                max_product, min_product = min_product,max_product

            min_product = min(nums[i],min_product * nums[i])
            max_product = max(nums[i],max_product * nums[i])

            ans = max(ans,max_product)

        return ans

s = Solution()
a = s.maxProduct([2, 3, 4])
print(a)
'''