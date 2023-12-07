class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # left=0
        # right=1
        # new_nums=[]
        # while left<right and right<len(nums):
        #     new_nums.append(str(nums[right])*nums[left])
        #     left+=2
        #     right+=2
        # new_nums=map(int,new_nums)
        # return new_nums
        new_nums = []
        for freq in range(0,len(nums)-1,2):
            for i in range(nums[freq]):
                new_nums.append(nums[freq+1])
        return new_nums