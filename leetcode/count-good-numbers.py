class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        if n%2 != 0:
            di = n//2
            re = n%2
            fi = di+1
            return pow(5,fi,mod)*pow(4,di,mod) % mod
        else:
            di = n//2
            return pow(5,di,mod)*pow(4,di,mod) % mod
