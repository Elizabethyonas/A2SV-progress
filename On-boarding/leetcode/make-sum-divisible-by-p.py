class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target_mod = sum(nums) % p
        
        if target_mod == 0:
            return 0
        
        prefix_sum = 0
        prefix_sums = {}
        prefix_sums[0] = -1
        min_length = len(nums)
        curr_sum_mod = 0
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            curr_sum_mod = (prefix_sum - target_mod + p) % p
            if curr_sum_mod in prefix_sums:
                min_length = min(min_length, i - prefix_sums[curr_sum_mod])
            prefix_sums[prefix_sum] = i
        
        return min_length if min_length < len(nums) else -1