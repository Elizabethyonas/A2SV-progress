class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        listsum=[]
        sum=0
        for i in nums:
            sum+=i
            listsum.append(sum)
        return listsum