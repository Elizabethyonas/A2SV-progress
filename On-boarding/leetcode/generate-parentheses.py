class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s, open, close):
            if open == close == n:
                ans.append(s)
            if open < n:
                backtrack(s + '(', open + 1, close)
            if close < open:
            
                backtrack(s + ')', open, close + 1)

            return None  
        backtrack("", 0, 0)
        return ans 