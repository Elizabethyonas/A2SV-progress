class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        reference={"[":"]", "(":")", "{":"}"}
        for char in s:
            if char in reference:
                stack.append(char)
            else:
                if len(stack) == 0 or char != reference[stack.pop()]:
                    return False
        return len(stack) == 0