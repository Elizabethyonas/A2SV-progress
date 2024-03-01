class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        added = 0

        for chr in s:
            if chr == "(":
                stack.append(chr)
            else:
                if stack:
                    stack.pop()
                else:
                    added += 1
        
        return added + len(stack)