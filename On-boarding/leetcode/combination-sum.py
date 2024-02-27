class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        check = defaultdict(int)
        def combination_sum(candidate, idx):
            if sum(candidate) > target :
                return 
            if sum(candidate) == target:
                ans.append(candidate.copy())
            for i in range(idx, len(candidates)):
                candidate.append(candidates[i])
                check[candidates[i]] += 1
                combination_sum(candidate, i)
                candidate.pop()

        combination_sum([], 0)
        return ans