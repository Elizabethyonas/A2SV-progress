class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        ones=0
        window_zeros=0

        for right in range(len(nums)):
            
            if nums[right]==0:
                window_zeros+=1

            while window_zeros>1:
                if nums[left]==0:
                    window_zeros-=1
                left+=1
            ones=max(ones,right-left)
        return ones
            
