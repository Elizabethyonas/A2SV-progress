class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j-1]
        for c1 in range(n):
            for c2 in range(c1, n):
                counter = collections.defaultdict(int)
                counter[0] = 1
                curr_sum = 0
                for r in range(m):
                    curr_sum += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                    count += counter[curr_sum - target]
                    counter[curr_sum] += 1
        
        return count