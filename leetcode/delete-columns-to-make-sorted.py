class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        i, n, m, count = 0, len(strs[0]), len(strs), 0
        while (i < n):
            for j in range(m-1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1 
                    break
            i += 1
        return count