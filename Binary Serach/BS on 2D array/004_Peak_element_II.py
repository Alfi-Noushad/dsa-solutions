class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        low = 0
        high = len(mat[0])-1

        while low <= high:
            mid = (low+high) // 2
            maxRow = 0

            for i in range(len(mat)):
                if mat[i][mid] > mat[maxRow][mid]:
                    maxRow = i
            current = mat[maxRow][mid]

            
            left = -1
            if mid > 0:
                left = mat[maxRow][mid - 1]
            
            right = -1
            if mid < len(mat[0])-1:
                right = mat[maxRow][mid + 1]
            
            if current > left and current > right:
                return [maxRow,mid]
            
            elif left > current:
                high = mid - 1
            else:
                low = mid + 1
            
s = Solution()
a = s.findPeakGrid([[5, 10, 8], [4, 25, 7], [3, 9, 6]])
print(a)


