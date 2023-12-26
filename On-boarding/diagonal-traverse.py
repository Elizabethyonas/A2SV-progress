class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        diagonally_traversed = [0] * (m * n)
        index = 0

        for sum in range(m + n - 1):
            if sum % 2 == 0:
                i = min(sum, m - 1)
                j = sum - i
                while i >= 0 and j < n:
                    diagonally_traversed[index] = mat[i][j]
                    index += 1
                    i -= 1
                    j += 1
            else:
                j = min(sum, n - 1)
                i = sum - j
                while j >= 0 and i < m:
                    diagonally_traversed[index] = mat[i][j]
                    index += 1
                    i += 1
                    j -= 1

        return diagonally_traversed
