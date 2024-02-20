class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        sum = 0
        for i, val in enumerate(arr):
            while stack and val < stack[-1][1]:
                j,v = stack.pop()
                left = j - stack[-1][0] if stack else j+1
                right = i - j
                sum = (sum+v*left*right) % mod
            stack.append((i,val))
        for i in range(len(stack)):
            j,n = stack[i]
            left = j - stack[i-1][0] if i > 0 else j+1
            right = len(arr) - j
            sum = (sum+n*left*right) % mod
        return sum
