class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float(inf)
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left,right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum==target:
                    return threeSum
                if abs(threeSum-target)<abs(closest_sum-target):
                    closest_sum=threeSum
                if threeSum>target:
                    right-=1
                else:
                    left+=1

                
        return closest_sum