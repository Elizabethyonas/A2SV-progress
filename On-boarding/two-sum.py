class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search = []
        for i in range(len(nums)):
            search.append((nums[i], i))
        search.sort()
        low = 0
        Up = len(nums) - 1
        while(low < Up) and search[low][0] + search[Up][0] != target:
            if search[low][0] + search[Up][0] < target:
                low += 1
            else:
                Up -= 1
        return [search[low][1], search[Up][1]]
        
        



            