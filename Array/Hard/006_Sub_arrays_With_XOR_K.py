class Solution:
    def subarraysWithXorK(self, nums, k):
        prefix_xor = 0
        mp = {0:1}
        count = 0

        for num in nums:
            prefix_xor ^= num
            need = prefix_xor ^ k
            if need in mp:
                count += mp[need]

            if prefix_xor in mp:
                mp[prefix_xor] += 1
            else:
                mp[prefix_xor] = 1
        return count
s = Solution()
a = s.subarraysWithXorK([4, 2, 2, 6, 4], 6)
print(a)