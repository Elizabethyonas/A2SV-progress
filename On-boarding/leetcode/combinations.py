class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i for i in range(1, n+1)]
        def backtrack(candidate, entry_index):

            if len(candidate) == k:
                ans.append(candidate[:])
                return
            if entry_index >= n:
                return
            # pick
            candidate.append(nums[entry_index])
            backtrack(candidate, entry_index + 1)
            candidate.pop()

            # not pick
            backtrack(candidate, entry_index + 1)
        backtrack([], 0)
        return ans