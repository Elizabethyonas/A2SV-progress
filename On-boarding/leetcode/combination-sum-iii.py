class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        self.backtrack(combinations, [], 1, k, n)
        return combinations
    def backtrack(self, combinations, path, start, k, target):
        if len(path) == k and target == 0:
            combinations.append(path[:])
            return
        
        for i in range(start, 10):
            if i > target:
                break
            path.append(i)
            self.backtrack(combinations, path, i + 1, k, target - i)
            path.pop()
    