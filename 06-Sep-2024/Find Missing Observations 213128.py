# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        av = mean * (n + len(rolls))
        missing = av - sum(rolls)
        if missing < n or missing > 6 * n:
            return []
        result = [1] * n
        remaining = missing - n  
        i = 0
        while remaining > 0:
            add_value = min(5, remaining)
            result[i] += add_value
            remaining -= add_value
            i += 1
        
        return result