class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        mp = {0: 1}
        count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in mp:
                count += mp[prefix_sum - k]

            if prefix_sum in mp:
                mp[prefix_sum] += 1
            else:
                mp[prefix_sum] = 1

        return count


s = Solution()
a = s.subarraySum([1, 1, 1], 2)
print(a)