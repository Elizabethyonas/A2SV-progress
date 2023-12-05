class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        tempc=[]
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                tempc.append(cnt)
                cnt=0
        tempc.append(cnt)
        return max(tempc)