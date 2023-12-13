class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1,r2,r3=set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        answer=[]
        for i in words:
            word=i.lower()
            if all(j in r1 for j in word) or all(j in r2 for j in word) or all(j in r3 for j in word):
                answer.append(i)
        return answer
            

                