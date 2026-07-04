class Solution(object):
    def painterPart(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low<=high:
            mid = (low+high) // 2
            paint = 0
            painter = 1
            for board in nums:
                if paint + board <= mid:
                    paint += board
                else:
                    painter += 1
                    paint = board
            if painter <= k:
                high = mid -1
            else:
                low = mid + 1

        return low
    
s = Solution()
a = s.painterPart([10, 20, 30, 40],2)
print(a)