class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(nums)
        first=0
        second=0
        while second<len(nums):
            if first==second:
                second+=1
            elif first!=second:
                if nums[first]==nums[second]:
                    nums[second]=101
                    k-=1
                    second+=1
                else:
                    first=second
        
        i=0 
        for j in range(len(nums)):
            if nums[j]-101:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

            
                
        return k