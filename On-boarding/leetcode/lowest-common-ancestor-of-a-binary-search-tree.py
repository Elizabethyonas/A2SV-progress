# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            curr_val = curr.val
            if p.val > curr_val and q.val > curr_val:
                curr = curr.right
            elif p.val < curr_val and q.val < curr_val:
                curr = curr.left
            else:
                return curr