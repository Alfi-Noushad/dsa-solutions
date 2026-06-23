class solution():
    def minSubArray(self,arr):
        sums = 0
        minsum = arr[0]
        for i in arr:
            sums += i
            minsum = min(minsum,sums)
        
            if sums > 0:
                sums = 0
        return minsum
s = solution()
a = s.minSubArray([3, -4, 2, -3, -1, 7, -5])
print(a)

