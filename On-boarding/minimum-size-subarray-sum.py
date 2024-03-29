class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        length=float('inf')
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                length=min(length, right-left+1)
                sum-=nums[left]
                left+=1
            
        return length if length != float('inf') else 0