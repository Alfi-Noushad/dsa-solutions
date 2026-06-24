class Solution:
    def spiralMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        ans = []
        while top <= bottom and left <= right:

            # Left -> Right
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1

            # Top -> Bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Right -> Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
a = s.spiralMatrix(matrix)
print(a)