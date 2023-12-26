class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_index=0
        count=0
        for index,val in enumerate(flips):
            if max_index<val:
                max_index=val
            if max_index==(index+1):
                count+=1
        return count

            
