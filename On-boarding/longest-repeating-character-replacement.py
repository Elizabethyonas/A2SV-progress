class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest, max_count = 0, 0, 0
        check = defaultdict(int)
        
        for right in range(len(s)):
            check[s[right]] += 1
            max_count = max(max_count, check[s[right]])
            while (right - left + 1) - max_count > k:
                check[s[left]] -= 1
                left += 1 
            longest = max(longest, right - left + 1)
        return longest
