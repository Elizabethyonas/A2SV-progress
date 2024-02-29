class Solution:
    def longestPalindrome(self, s: str) -> int:
        check = defaultdict(int)
        max_s = 0
        odd = 0
        s = list(s)
        for chr in s:
            check[chr] += 1
        for chr in check:
            if check[chr] % 2 == 0:
                max_s += check[chr]
            else:
                print(chr, odd)
                max_s += check[chr] - 1
                odd = 1
        return max_s + odd