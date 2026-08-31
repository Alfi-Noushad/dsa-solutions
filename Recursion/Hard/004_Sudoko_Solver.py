class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def isValid(row,col,num):
            if num in board[row]:
                return False
            
            for r in range(9):
                if board[r][col] == num:
                    return False

                    
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3

            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if board[r][c] == num:
                        return False

            return True

        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in "123456789":
                            if isValid(row,col,num):
                                board[row][col] = num

                                if solve():
                                    return True

                                board[row][col] = "."
                        return False
            return True

        solve()
        