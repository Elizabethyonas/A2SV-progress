class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left=0
        right=n
        new_array=[]
        while left<right and right<len(nums):
            new_array.append(nums[left])
            new_array.append(nums[right])
            left+=1
            right+=1
        return new_array