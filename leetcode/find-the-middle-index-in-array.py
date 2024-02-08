class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            prefix.append(sum)
        
        n=len(prefix)
        for j in range(n):
            leftSum=prefix[j-1] if j>0 else 0
            rightSum=prefix[n-1]-prefix[j]
            if leftSum==rightSum:
                return j
        return -1