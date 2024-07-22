# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def valid(i, j):
            return 0 <= i < n and 0<= j < n
        n = len(matrix)
        dp = [[float('inf') for i in range(n)] for j in range(n)]

        for k in range(n):
            dp[0][k] = matrix[0][k]

        for i in range(n - 1):
            for j in range(n):
                if valid(i + 1, j - 1):
                    dp[i + 1][j - 1] = min(dp[i][j] + matrix[i + 1][j - 1], dp[i + 1][j - 1])
                if valid(i + 1, j):
                    dp[i + 1][j] = min(dp[i][j] + matrix[i + 1][j], dp[i + 1][j])
                if valid(i + 1, j + 1):
                    dp[i + 1][j + 1] = min(dp[i][j] + matrix[i + 1][j + 1], dp[i + 1][j + 1])
        
        return min(dp[-1])
        