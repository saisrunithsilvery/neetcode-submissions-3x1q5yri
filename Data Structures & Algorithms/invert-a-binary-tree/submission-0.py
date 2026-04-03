# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None


        if root.left and root.right:

            x= root.left
            root.left = root.right
            root.right = x
            self.invertTree(root.right)
            self.invertTree(root.left)

        elif root.left:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)

        elif root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)

        return root

                    

        