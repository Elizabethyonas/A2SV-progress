class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new = nums * 2
        n = len(nums)
        stack = []
        ans = [-1] * len(new)
        
        for i, val in enumerate(new):
            while stack and stack[-1][1] < val:
                ans[stack[-1][0]] = val
                stack.pop()
            stack.append((i,val))
        return ans[:n]