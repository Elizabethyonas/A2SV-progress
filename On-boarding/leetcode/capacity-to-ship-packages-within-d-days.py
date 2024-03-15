class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high
        def helper(capacity):
            curr_sum = 0
            day = 1
            for i in range(len(weights)):
                if curr_sum + weights[i] > capacity:
                    day += 1
                    curr_sum = 0
                curr_sum += weights[i]
            return day <= days

        while low < high:
            mid = low + (high - low) // 2
            if helper(mid):
                high = mid
                ans = min(ans, mid)
            else:
                low = mid + 1
        return ans