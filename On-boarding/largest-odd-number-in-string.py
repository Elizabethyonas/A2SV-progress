class Solution:
    def largestOddNumber(self, num: str) -> str:
        num=num[::-1]
        for numbr in num:
            if int(numbr)%2!=0:
                return num[num.index(numbr):][::-1]
        return "" 