class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=('a','e','i','o','u')
        left=0
        window=0
        count=0
        for i in range(k):
            if s[i] in vowel:
                window+=1
                count=max(count,window)
        for right in range(k,len(s)):
            if s[right] in vowel:
                window+=1
            if s[left] in vowel:
                window-=1
            count=max(count,window)
            left+=1

        return count
        
            