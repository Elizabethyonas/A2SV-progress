class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split())
        s.reverse()
        return ' '.join(s)