# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max1 = float('-inf')
        if not root:
            return 0

        def dfs(root):
            if not root:
                return 0          # ✅ clean

            left = dfs(root.left)    
            right = dfs(root.right)

            if left < 0: left = 0
            if right < 0: right = 0

            self.max1 = max(left+right+root.val, self.max1)
            return root.val + max(left, right)

        return dfs(root)        