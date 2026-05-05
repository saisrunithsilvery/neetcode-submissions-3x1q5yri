# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([root])

        while q:
            x = q.popleft()
            x.left, x.right = x.right, x.left  # always swap, even if None

            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)

        return root