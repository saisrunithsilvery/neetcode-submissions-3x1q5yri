# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None

        def max1(node):

            if not node:
                return 
            x = 0
            if node.left :
                x = max1(node.left)
            y =0
            if node.right:
                y = max1(node.right)    

            return 1+ max(x, y)
        return max1(root)        
        