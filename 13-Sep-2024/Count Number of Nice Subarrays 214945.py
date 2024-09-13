# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count=0
        left=0
        subarray_count=0
        ans=0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                odd_count+=1
                subarray_count=0
            while odd_count==k:
                if nums[left]%2!=0:
                    odd_count-=1
                subarray_count+=1
                left+=1
            
            ans+=subarray_count
        return ans
