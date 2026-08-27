class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()

        def solve(row):
            if row == n:
                result = []
            
                for r in board:
                    result.append("".join(r))
                ans.append(result)
                return
            
            for col in range(n):
                if col in cols:
                    continue
                if row-col in diag1:
                    continue
                if row+col in diag2:
                    continue
                
                board[row][col] = "Q"

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                solve(row + 1)

                board[row][col] = "."

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        solve(0)


        return ans

        