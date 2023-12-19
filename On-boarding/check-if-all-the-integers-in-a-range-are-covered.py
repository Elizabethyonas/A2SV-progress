class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left,right+1):
            flag=False
            for i in range(len(ranges)):
                if num in range(ranges[i][0],ranges[i][1]+1):
                    flag=True
                    break
            if num not in range(ranges[i][0],ranges[i][1]+1):
                return False
        return True
        