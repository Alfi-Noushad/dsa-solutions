class Solution:
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        row = [0]*r
        col = [0]*c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(r):
            for j in range(c):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
        return matrix
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
s.setZeroes(matrix)
for r in matrix:
    print(r)

