class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=max(candies)
        res=[]
        for i in range(len(candies)):
            c=candies[i]+extraCandies
            res.append(c>=x)
        return res