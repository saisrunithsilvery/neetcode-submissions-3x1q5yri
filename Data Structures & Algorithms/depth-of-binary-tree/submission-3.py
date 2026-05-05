# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        
        def solve(Node):

            if not Node :
                return 0

            right = 1 + solve(Node.right)
            left = 1 + solve(Node.left)

            return max(right, left)

        return solve(root)        


    
        