class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)//4
        freq=Counter(arr)
        only_values=set(arr)
        for val in only_values:
            if freq[val]>n:
                return val