class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = self.hepler(x, abs(n))
        return ans if n > 0 else 1/ans
    def hepler(self, x, n):
        if n == 0:
            return 1
        ans = self.myPow(x, n//2)
        if n%2 == 0:
            return ans * ans
        else:
            return ans * ans * x