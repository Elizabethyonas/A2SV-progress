class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        def helper(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h
        while low < high:  
            mid = low + (high - low) // 2
            if helper(mid):
                high = mid  
                ans = min(ans, mid)
            else:
                low = mid + 1
        return ans  