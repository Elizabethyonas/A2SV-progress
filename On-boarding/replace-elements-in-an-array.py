class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {num: i for i, num in enumerate(nums)}
        for o, e in operations:
            i = dic[o]
            nums[i] = e
            dic[e] = i
            del dic[o]
        return nums
        