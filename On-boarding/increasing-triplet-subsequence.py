class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first= inf
        second= inf
        for i in range(len(nums)):
            print(first,second)
            if  nums[i] > second:
                return True
            if nums[i] <= first:
                first = nums[i]
                continue
            if nums[i] < second:
                second = nums[i]
        return False
     