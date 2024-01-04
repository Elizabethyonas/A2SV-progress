class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while left<right and right<len(nums):
            sum=nums[left]+nums[right]
            if sum<target:
                count+=1
                right-=1
            elif sum>=target:
                right-=1
            if left==right:
                left+=1
                right=len(nums)-1
        return count