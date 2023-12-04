class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wd1=""
        wd2=""
        for i in range(len(word1)):
            wd1+=word1[i]
            i+=1
        for i in range(len(word2)):
            wd2+=word2[i]
            i+=1
        if wd1==wd2:
            return True
        else:
            return False