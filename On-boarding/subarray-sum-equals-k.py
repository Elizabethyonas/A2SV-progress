class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        total_count = 0

        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            total_count += count[complement]
            count[prefix_sum] += 1

        return total_count
