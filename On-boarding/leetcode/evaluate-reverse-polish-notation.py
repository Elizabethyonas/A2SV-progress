class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for chr in tokens: 
            if chr != "*" and chr != "/" and chr != "-" and chr != "+":
                stack.append(chr)
            else:
                if len(stack) > 1:
                    second = stack.pop()
                    first = stack.pop()
                    if chr == "*":
                        res = int(first) * int(second)
                        stack.append(str(res))
                    elif chr == "+":
                        res = int(first) + int(second)
                        stack.append(str(res))
                    elif chr == "/":
                        res = int(int(first) / int(second))
                        stack.append(str(res))
                    else:
                        res = int(first) - int(second)
                        stack.append(str(res))
        return int(stack[-1])
        