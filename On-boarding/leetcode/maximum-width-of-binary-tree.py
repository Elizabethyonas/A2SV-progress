# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [1]
        max_width = 1
        q = deque([root] if root else [])
        while q:
            level = []
            length = len(q)
            for i in range(length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    level.append(ans[i] * 2)
                if node.right:
                    level.append((ans[i] * 2) + 1)
                    q.append(node.right)
            if not level:
                continue
            max_width = max(max_width, level[-1] - level[0] + 1)
            ans = level
        return max_width
            

            # print(ans)
        # for i in range(len(ans)-1):
        #     curr = ans[i][-1] - ans[i][0] + 1
        #     max_width = max(curr, max_width)
        # return max_width