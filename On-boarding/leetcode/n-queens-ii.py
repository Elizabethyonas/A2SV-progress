class Solution:
    def totalNQueens(self, n: int) -> int:
        diag1 = set()
        diag2 = set()
        col = set()
        
        res = 0
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            for c in range(n):
                if c in col or (r+c) in diag1 or (r-c) in diag2:
                    continue
                col.add(c)
                diag1.add(r+c)
                diag2.add(r-c)
                backtrack(r+1)

                col.remove(c)
                diag1.remove(r+c)
                diag2.remove(r-c)
                
        backtrack(0)
        return res