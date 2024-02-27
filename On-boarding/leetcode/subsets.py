class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        def backtrack(candidate, idx):
            
            # if candidate not in ans:
            if idx >= len(nums):
                return
                
            
            # pick
            candidate.append(nums[idx])
            ans.append(candidate[:])

            backtrack(candidate, idx + 1)
            candidate.pop()

            # not pick
            backtrack(candidate, idx + 1)
        backtrack([], 0)
        return ans