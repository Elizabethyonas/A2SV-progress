class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if all([num < 0 for num in nums]): return max(nums)
        max_so_far, curr_sum = 0, 0
        if len(nums)==1 and nums[0] < 0:
            return nums[0]
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum < 0:
                curr_sum = 0
            max_so_far = max(max_so_far, curr_sum)
        return max_so_far