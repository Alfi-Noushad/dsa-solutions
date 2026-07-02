class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low = 1
        high = max(nums)

        while low<=high:
            total = 0
            mid = (low+high)//2
            for i in nums:
                total += (i +mid-1) // mid
            if total <= threshold:
                high = mid -1
            else:
                low = mid + 1
        return low

s = Solution()
a = s.smallestDivisor([1,2,3,4,5],8)
print(a)

        