class Solution:
    def minimizedStringLength(self, s: str) -> int:
        unique_char=set()
        for char in s:
            if char not in unique_char:
                unique_char.add(char)
            else:
                continue
        return len(unique_char)