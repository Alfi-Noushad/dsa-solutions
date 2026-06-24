class Solution:
    def rotateMatrix(self, matrix):
        r = len(matrix)
        for i in range(r):
            for j in range(i+1,r):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(r):
            matrix[i].reverse()
        
        return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
s.rotateMatrix(matrix)
for r in matrix:
    print(r)