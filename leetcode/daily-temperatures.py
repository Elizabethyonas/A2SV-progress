class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i,val))
        while stack:
            ans[stack[-1][0]] = 0
            stack.pop()

        return ans