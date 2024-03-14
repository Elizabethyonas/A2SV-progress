class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        freq = defaultdict(list)
        for i in range(len(nums)):
            freq[nums[i]].append(i)
        return [freq[target][0], freq[target][-1]]