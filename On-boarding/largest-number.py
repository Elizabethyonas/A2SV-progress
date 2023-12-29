class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(reverse=True)
        for i,v in enumerate(nums):
            nums[i]=str(v)
        for i in range(len(nums)):
            for i in range(len(nums)-1):
                if int(nums[i] + nums[i+1]) <= int(nums[i+1] + nums[i]):
                    nums[i],nums[i+1] = nums[i+1],nums[i]
        if nums[0]=="0":
            return "0"
        return ''.join(nums)
            
            