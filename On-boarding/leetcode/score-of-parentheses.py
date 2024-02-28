class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score, curr = 0, 0 
        stack = []
        for chr in s:
            if chr == "(":
                stack.append(0)
            else:
                multi = stack.pop()
                if multi == 0:
                    curr = 1
                else:
                    curr =  2*multi
                if stack:
                    stack[-1] += curr
                else:
                    score += curr
        return score