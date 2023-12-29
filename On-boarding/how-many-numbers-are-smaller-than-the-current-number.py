class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        result = []
        for num in nums:
            count = sum(counter[k] for k in counter if k < num)
            result.append(count)

        return result