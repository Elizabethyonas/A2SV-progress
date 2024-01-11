class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left, shortest = 0, float('inf')
        check=defaultdict(int)
        for right in range(len(cards)):
            check[cards[right]]+=1
            
            while check[cards[right]] == 2:
                shortest=min(shortest,right-left+1)
                check[cards[left]]-=1
                left+=1
            
            
            
        return (shortest if shortest!=float('inf') else -1)