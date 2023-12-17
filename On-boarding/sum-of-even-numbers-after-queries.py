class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer=[]
        even_sum=0
        for num in nums:
            if num%2==0:
                even_sum+=num
        for val, i in queries:
            if nums[i]%2==0:
                even_sum-=nums[i]
            nums[i]+=val
            if nums[i]%2==0:
                even_sum+=nums[i]
            answer.append(even_sum)
        return answer