class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()  
        result = []
        for i in range(n):
            result.append(0)  
        indices = list(range(n))  
        for card in deck:
            result[indices.pop(0)] = card  
            if indices: 
                indices.append(indices.pop(0))  
        return result