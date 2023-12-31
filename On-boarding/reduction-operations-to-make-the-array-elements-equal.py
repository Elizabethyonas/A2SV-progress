class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        maxNum=max(nums)
        freq=[0]*(maxNum+1)
        for num in nums:
            freq[num]+=1
        freq = list(filter(None, freq))
        operation=0
        if len(freq)==1:
            return operation
        for i in range(len(freq)-1,0,-1):
            operation+=freq[i]
            freq[i-1] += freq[i]
        
        return operation