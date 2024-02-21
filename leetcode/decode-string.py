class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            temp = ""
            num = ""
            if s[i] != "]":
                stack.append(s[i])
            if s[i] == "]":
                while stack and stack[-1] != "[":
                    temp = stack[-1] + temp
                    stack.pop()
                if stack[-1] == "[":
                    stack.pop()
                while stack and stack[-1].isdigit():
                    num = str(stack[-1]) + num
                    stack.pop()
                
                stack.append(temp*(int(num)))
        return ''.join(stack)