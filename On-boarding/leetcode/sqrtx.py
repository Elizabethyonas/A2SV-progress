class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 1,x
        while left<=right:
            middle = (left+right)//2
            if middle**2==x:
                return middle
            elif middle**2>x:
                right = middle-1
            else:
                left = middle+1
        return left-1