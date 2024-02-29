class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        counter = 0
        steps = 0
        while target > 1:
            if target % 2 == 0 and counter < maxDoubles:
                target = target // 2
                steps += 1
                counter += 1
            else:
                target -= 1
                steps += 1
            if counter == maxDoubles:
                return steps + target - 1

                
        return steps