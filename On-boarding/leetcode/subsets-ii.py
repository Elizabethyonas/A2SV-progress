class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        
        def backtrack(candidate, idx):
            if candidate not in ans:
                ans.append(candidate[:])
            if idx >= len(nums):
                return
            # pick
            candidate.append(nums[idx])
            backtrack(candidate, idx + 1)
            candidate.pop()

            # not pick
            backtrack(candidate, idx + 1)
        backtrack([], 0)
        return ans