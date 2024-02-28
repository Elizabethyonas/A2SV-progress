class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        prefix = 0
        ans = []
        for i,num in enumerate(nums):
            right_sum = total_sum - num - prefix
            left = (num*i) - prefix
            right = right_sum - (len(nums)- i -1)* num
            ans.append(left + right)
            prefix += num
        return ans