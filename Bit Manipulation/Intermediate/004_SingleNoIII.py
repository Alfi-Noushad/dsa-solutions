class Solution:
    def twoOddNum(self,nums):
        xor_all = 0

        for num in nums:
            xor_all ^= num

        mask = xor_all & (-xor_all)

        a = 0
        b = 0

        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num

        return [a,b]

s = Solution()
a = s.twoOddNum([1, 2, 1, 3, 5, 2])
print(a)