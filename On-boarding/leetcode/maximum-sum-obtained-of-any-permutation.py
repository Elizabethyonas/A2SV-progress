class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * n
        for start, end in requests:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        count.sort(reverse=True)
        nums.sort(reverse=True)
        max_sum = 0
        mod = 10**9 + 7
        for i in range(n):
            max_sum = (max_sum + nums[i] * count[i]) % mod
        
        return max_sum