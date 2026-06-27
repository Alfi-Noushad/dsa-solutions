class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)

        xr = 0
        xr_org = 0

        repeating = 0
        missing = 0

        for i in range(n):
            xr ^= nums[i]

            xr_org ^= i+1

        #missing ^ repeating o/p
        number = xr ^xr_org

        #find rightmost bit
        diff_bit = number & -number

        a = 0 # zero on
        b = 0 # one on

        for i in range(n):
            if nums[i] & diff_bit:
                b ^= nums[i]
            else:
                a ^= nums[i]
            if  (i + 1) & diff_bit:
                b ^= (i + 1)
            else:
                a ^= (i + 1)
        
        for x in nums:
            if x == a:
                repeating = a
                missing = b
                return [repeating,missing]
            else:
                repeating = b
                missing = a
                return [repeating,missing]


s = Solution()
a = s.findMissingRepeatingNumbers([1, 2, 3, 6, 7, 5, 7])
print(a)


