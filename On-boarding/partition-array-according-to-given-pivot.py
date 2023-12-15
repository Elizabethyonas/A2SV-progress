class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater=[]
        less=[]
        pivots=[]
        for num in nums:
            if num>pivot:
                greater.append(num)
            elif num<pivot:
                less.append(num)
            else:
                pivots.append(num)
        
        
        return less+pivots+greater

