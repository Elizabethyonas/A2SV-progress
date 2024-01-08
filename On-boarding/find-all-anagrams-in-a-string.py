class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = defaultdict(int)
        for char in p:
            target[char] += 1
        
        k = len(p)
        i = 0
        j = 0
        match_count = 0
        ans = []
        while j < len(s):
            if target[s[j]] > 0:
                match_count += 1
            target[s[j]] -= 1
            j += 1
            if j - i > k:
                if target[s[i]] >= 0:
                    match_count -= 1
                target[s[i]] += 1
                i += 1
            if match_count == k:
                ans.append(i)
        return ans

                
            