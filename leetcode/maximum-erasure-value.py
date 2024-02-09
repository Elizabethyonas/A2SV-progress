class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        unique = set()
        start = end = 0
        maxScore = 0
        windowSum = 0

        while end < n:
            if nums[end] not in unique:
                unique.add(nums[end])
                windowSum += nums[end]
                end += 1
                maxScore = max(maxScore, windowSum)
            else:
                unique.remove(nums[start])
                windowSum -= nums[start]
                start += 1

        return maxScore