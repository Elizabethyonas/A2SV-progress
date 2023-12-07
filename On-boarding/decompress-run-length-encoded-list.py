class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        left=0
        right=1
        new_nums=[]
        while left<right and right<len(nums):
            s1=[str(nums[right])]
            duplicate=s1*nums[left]
            new_nums.append(duplicate)
            left+=2
            right+=2
        new_nums=[int(x) for sublist in new_nums for x in sublist]
        return new_nums
        