class Solution:
    def upperBound(self, row, target):
        low = 0
        high = len(row) - 1
        ans = len(row)

        while low <= high:
            mid = (low + high) // 2

            if row[mid] > target:   
                ans = mid   
                high = mid - 1
            else:
                low = mid + 1
        return ans
    def findMedian(self, matrix):
        low = matrix[0][0]
        high = matrix[0][-1]

        for row in matrix:
            low = min(low, row[0])
            high = max(high, row[-1])

        rows = len(matrix)
        cols = len(matrix[0])

        required = (rows * cols) // 2
        while low<= high:
            mid = (low+high) // 2
            count = 0
            for row in matrix:
                count += self.upperBound(row, mid)

            if count <= required:
                low = mid+1
            else:
                high = mid - 1
        return low

s = Solution()
a =s.findMedian([ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] )
print(a)
            