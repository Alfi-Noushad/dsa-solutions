class Solution:
    def NthRoot(self, n, m):
        low = 1
        high = m

        while low <= high:
            mid = (low+high)//2
            if mid**n <= m:
                ans = mid
                low = mid+1
            else:
                high = mid -1
        return ans

s= Solution()
a = s.NthRoot(3,27)
print(a)