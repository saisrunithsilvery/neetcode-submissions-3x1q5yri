# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max1 = 0

        def dfs(node):
            nonlocal max1

            if not node :
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max1 = max(max1, left+right)   

            return 1+ max(left, right) 

        dfs(root)    

        return max1