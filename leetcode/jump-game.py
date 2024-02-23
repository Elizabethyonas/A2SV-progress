class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums) - 1
        j=good-1
        while j>=0:
            diff= good - j
            if nums[j]>=diff:
                good=j
            j-=1
        return good==0