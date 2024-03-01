class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palin = list(palindrome)
        n = len(palin)
        if len(palindrome) == 1:
            return ""
        for i in range(n // 2):
            if palin[i] != "a":
                palin[i] = "a"
                return "".join(palin)
        
        palin[-1] = "b"
        return "".join(palin)