class Solution:
    def minimumSteps(self, s: str) -> int:
        prefix=[]
        sum=0
        steps=0
        
        for i in range(len(s)):
            sum+=int(s[i])
            prefix.append(sum)
        # print(prefix)
        for j in range(len(s)):
            if s[j]=='0':
                # print(s[j])
                steps+=prefix[j-1] if j>0 else 0
        return steps

