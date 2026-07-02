class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low+high)//2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

s = Solution()
a = s.minEatingSpeed([7, 15, 6, 3],8)
print(a)
        