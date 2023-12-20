class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        original=capacity
        for plant,water in enumerate(plants):
            if capacity>=water:
                steps+=1
            else:
                capacity=original
                steps+=plant+plant+1
            capacity-=water
        return steps