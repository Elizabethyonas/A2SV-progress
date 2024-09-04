# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        str_num = ''.join(str(ord(chr) - ord('a') + 1) for chr in s)
        num = sum(int(digit) for digit in str_num)
        for i in range(k - 1):
            num = sum(int(digit) for digit in str(num))
        return num