class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = [0] * n
        max_col = [0] * n
        for i in range(n):
            for j in range(n):
                max_row[i] = max(max_row[i], grid[i][j])
                max_col[j] = max(max_col[j], grid[i][j])
        
        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_height = min(max_row[i], max_col[j])
                increase = max_height - grid[i][j]
                total_increase += increase
        
        return total_increase