class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s=[]
        index=0
        for space in spaces:
            new_s.append(s[index:space])
            index=space
        new_s.append(s[index:])
        return ' '.join(new_s)

            