class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        ans=[]
        max_word= max(len(word) for word in words)
        for i in range(max_word):
            temp=[]
            for word in words:
                temp.append(word[i] if i<len(word) else ' ')
            ans.append(''.join(temp).rstrip())
        return ans
