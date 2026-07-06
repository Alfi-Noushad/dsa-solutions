class Solution:
    def lowerBound(self, row):
        low = 0
        high = len(row)-1
        ans = len(row)

        while low <= high:
            mid = (low+high) // 2

            if row[mid] >= 1:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def rowWithMax1s(self,mat):
        max_ones = 0
        for i in range(len(mat)):
            idx = self.lowerBound(mat[i])
            max_ones = max(max_ones,idx)
        return max_ones


s = Solution()
a =s.rowWithMax1s([[1, 1, 1], [0, 0, 1], [0, 0, 0]])
print(a)