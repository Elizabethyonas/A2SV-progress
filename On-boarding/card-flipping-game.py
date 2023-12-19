class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        dict_reference=defaultdict(int)
        result=[]
        for i,j in zip(fronts,backs):
            dict_reference[i]=1
            dict_reference[j]=1
        for i,j in zip(fronts,backs):
            if i==j and i in dict_reference:
                del dict_reference[i]
        if dict_reference:
            return min(dict_reference.keys())
        else:
            return 0