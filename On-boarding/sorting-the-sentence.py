class Solution:
    def sortSentence(self, s: str) -> str:
        index={}
        s=list(s.split(" "))
        ans=[]
        for char in s:
            index[char[-1]]=char[:-1]
        
        for i in range(len(index)):
            ans.append(index[str(i+1)])
        return ' '.join(ans)


