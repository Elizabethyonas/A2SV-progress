class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        left = mx = 0
        x  = ""
        for i in range(len(s)): 
            ans = ""
            mp = set()
            for j in range(i, len(s)):
                ans += s[j]
                mp.add(s[j])

                flag = True
                for val in ans: 
                    if val.isupper(): 
                        if val.lower() not in mp: 
                            flag = False
                            break
                    if val.islower():
                        if val.upper() not in mp:
                            flag = False
                            break
                
                if flag == True:
                    if len(ans) > mx: 
                        x = ans
                        mx = len(ans)
            

        return x