# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        check = []
        ans = []
        def inorderTraversal(root):
            if not root: 
                return None
            inorderTraversal(root.left)
            check.append(root.val)
            inorderTraversal(root.right)
        inorderTraversal(root)
        for num in check:
            freq[num] += 1
        mode = max(freq.values())
        check_set = set(check)
        for num in check_set:
            # print(num, mode)
            if freq[num] == mode :
                ans.append(num)
        return ans