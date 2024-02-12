class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        check = defaultdict(int)
        window = defaultdict(int)
        left = 0
        count = 0
        distinct = 0
        
        for num in nums:
            if check[num] == 0:
                distinct += 1
            check[num] += 1
        
        for right in range(len(nums)):
            window[nums[right]] += 1
            
            while len(window) == distinct:
                count += len(nums) - right
                window[nums[left]] -= 1
                
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                
                left += 1
        
        return count