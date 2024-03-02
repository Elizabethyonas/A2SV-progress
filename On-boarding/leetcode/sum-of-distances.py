class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        left_count = defaultdict(int)
        left_sum = defaultdict(int)

        for i, val in enumerate(nums):
            ans[i] += left_count[val] * i
            ans[i] -= left_sum[val]
            left_count[val] += 1
            left_sum[val] += i

        right_count = defaultdict(int)
        right_sum = defaultdict(int)

        for i, val in reversed(list(enumerate(nums))):
            ans[i] += right_sum[val]
            ans[i] -= right_count[val] * i
            right_count[val] += 1
            right_sum[val] += i
        return ans