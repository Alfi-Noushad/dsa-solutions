class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(matrix)-1
        ans = 0

        while low<=high:
            mid = (low+high) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] > target:
                high = mid - 1
            else:
                low = mid+1
        return False
    def rowMatrix(self,mat,target):
        for i in range(len(mat)):
            if self.searchMatrix(mat[i],target):
                return True
        return False
    
s = Solution()
a = s.rowMatrix( [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ],1)
print(a)
        