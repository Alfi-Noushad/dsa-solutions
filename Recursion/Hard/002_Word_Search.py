class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        def solve(row,col,index):
            if row<0 or row >= rows or col <0 or col>= cols:
                return False
            if board[row][col] != word[index]:
                return False
            
            if index == len(word)-1:
                return True
            
            temp = board[row][col]
            board[row][col] = "#"

            found = (
                solve(row - 1, col, index + 1) or
                solve(row + 1, col, index + 1) or
                solve(row, col - 1, index + 1) or
                solve(row, col + 1, index + 1)
            )
            board[row][col] = temp

            return found
        for row in range(rows):
            for col in range(cols):
                if solve(row, col, 0):
                    return True

        return False
        solve(row,col,0)
        