class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        summ = sum(nums[:k]) 
        maxi = summ / k 
        while r < len(nums):
            summ = summ - nums[l] + nums[r] 
            av = summ / k 
            if av > maxi:
                maxi = av  
            l += 1
            r += 1
        return maxi