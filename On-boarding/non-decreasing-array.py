class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modify=0
        for i in range(len(nums)) :
            if i+1<len(nums) and nums[i]>nums[i+1]:
                modify+=1
                if i-1>=0 and nums[i-1]>nums[i+1]:
                     nums[i+1]=nums[i]
            else:
                continue
        if modify>1:
            return False
        return True