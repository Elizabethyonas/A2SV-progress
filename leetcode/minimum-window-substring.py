
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        required = len(t_counts)
        formed = 0
        window_counts = Counter()
        left = 0
        min_window = float('inf'), None, None
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1
            
            if char in t_counts and window_counts[char] == t_counts[char]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < min_window[0]:
                    min_window = right - left + 1, left, right
                window_counts[s[left]] -= 1
                if s[left] in t_counts and window_counts[s[left]] < t_counts[s[left]]:
                    formed -= 1
                left += 1
        
        return "" if min_window[0] == float('inf') else s[min_window[1]:min_window[2]+1]