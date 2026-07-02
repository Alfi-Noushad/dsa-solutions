class Solution:
    def floorSqrt(self, n):
        low = 1
        high = n

        while low <= high:
            mid = (low+high)//2
            if mid**2 <= n:
                ans = mid
                low = mid+1
            else:
                high = mid -1
        return ans

s= Solution()
a = s.floorSqrt(36)
print(a)