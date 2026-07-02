class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low<=high:
            flowerbl = 0
            bouquets = 0
            mid = (low+high)//2
            for i in bloomDay:
                if i <= mid:
                    flowerbl += 1
                else:
                    bouquets += flowerbl // k
                    flowerbl = 0
            bouquets += flowerbl // k

            if bouquets >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
s= Solution()
a = s. minDays([7, 7, 7, 7, 13, 11, 12, 7],3,2)
print(a)
        