# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]

        for char in s:
            if(char=="#" and not stack1):
                continue
            if(stack1):
                if( char=="#"):
                    stack1.pop()
                    continue
            stack1.append(char)
        
        for char in t:
            if(char=="#" and not stack2):
                continue
            if(stack2):
                if( char=="#"):
                    stack2.pop()
                    continue
            stack2.append(char)

        return stack1==stack2