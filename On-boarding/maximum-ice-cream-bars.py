class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars=0
        sum=0
        for price in costs:
            sum+=price
            if sum<=coins:
                
                bars+=1
            else:
                break
        return bars