# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_array = []
        
        def inorderTraversal(root):
            if root is None:
                return
            inorderTraversal(root.left)
            sorted_array.append(root.val)
            inorderTraversal(root.right)
        
        inorderTraversal(root)
        return sorted_array[k-1]
        
