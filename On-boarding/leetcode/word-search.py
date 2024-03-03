class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        paths = set()
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if row < 0 or col < 0 or row >= rows or col >= cols or word[i] != board[row][col] or (row, col) in paths:
                return False
            
            paths.add((row, col))
            ans = (dfs(row + 1, col, i + 1) or
                   dfs(row - 1, col, i + 1) or
                   dfs(row, col + 1, i + 1) or
                   dfs(row, col - 1, i + 1))
            
            paths.remove((row, col))
            return ans
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False