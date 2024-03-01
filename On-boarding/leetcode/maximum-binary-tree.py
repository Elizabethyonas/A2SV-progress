# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(prefix, idx):
            if not prefix:
                return None
            print(prefix)
            roo = max(prefix)
            for i in range(len(prefix)):
                if prefix[i] == roo:
                    idx = i
            root = TreeNode(roo)
            root.left  = divide(prefix[:idx], idx)

            root.right = divide(prefix[idx+1:], idx)

            return root
        return divide(nums, 0)
        