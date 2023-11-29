class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for st in range(len(strs[0])):
            count = 1
            for i in range(1,len(strs)):
                if st < len(strs[i]):
                    if strs[i][st] == strs[0][st]:
                        count += 1
            if count == len(strs):
                res += strs[0][st]
            else:
                break
        return res
            
           