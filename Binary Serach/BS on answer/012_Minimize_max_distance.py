from math import ceil
class Solution:
    def minimiseMaxDistance(self, arr, k):
        low = 0.0
        high = 0.0
        for i in range(len(arr) - 1):
            gap = arr[i + 1] - arr[i]
            high = max(high, gap)

        while high - low > 1e-6:
            mid = (low + high) / 2

            needed = 0
            for i in range(len(arr) - 1):
                gap = arr[i + 1] - arr[i]
                # Calculate how many new stations are needed
                stations = ceil(gap/mid)-1
                needed += stations

            if needed <= k:
                high = mid
            else:
                low = mid
        return high
        
s =Solution()
a = s.minimiseMaxDistance([1,2,3,4,5],4)
print(a)
           