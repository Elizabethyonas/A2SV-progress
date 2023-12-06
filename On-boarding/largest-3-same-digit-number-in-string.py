class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_int=""
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                if num[i]>=max_int:
                    max_int=num[i]
        return max_int*3