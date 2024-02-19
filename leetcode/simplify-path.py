class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        reference=path.split('/')
        for char in reference:
            if char == ".." and len(stack) > 0:
                stack.pop()
            elif char != '.' and  char != '' and char != "..":
                stack.append(char)
        return '/' + '/'.join(stack)
