class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low<=high:
            mid = (low+high) // 2
            val = 0
            subarrays = 1
            for no in nums:
                if val + no <= mid:
                    val += no
                else:
                    subarrays += 1
                    val = no
            if subarrays <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
s = Solution()
a = s.splitArray([1,2,3,4,5],3)
print(a)

        