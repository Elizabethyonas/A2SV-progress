class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix_0 = [0] * len(s)
        prefix_1 = [0] * len(s)
        res = 0
        for i in range(len(s)):
            if s[i] == "0" :
                prefix_0[i] += 1
        for i in range(len(s)):
            if s[i] == "1" :
                prefix_1[i] += 1
        for i in range(1,len(prefix_0)):
            prefix_0[i] += prefix_0[i - 1]
        for i in range(1,len(prefix_1)):
            prefix_1[i] += prefix_1[i - 1]
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                res += prefix_1[i-1] * (prefix_1[-1] - prefix_1[i])
            else:
                res += prefix_0[i-1] * (prefix_0[-1] - prefix_0[i])
        
        return res